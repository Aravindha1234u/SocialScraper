import calendar
import json
import os
import platform
import sys
import urllib.request
import yaml

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Global Variables
try:
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
except DeprecationWarning as e:
    pass

# whether to download photos or not
download_uploaded_photos = True
download_friends_photos = True

friends_small_size = True
photos_small_size = True

total_scrolls = 2500
current_scrolls = 0
scroll_time = 8

with open("./social/selectors.json") as json_file:
    selectors = json.load(json_file)

old_height = 0
firefox_profile_path = selectors.get("firefox_profile_path")
facebook_https_prefix = selectors.get("facebook_https_prefix")
facebook_link_body = selectors.get("facebook_link_body")

def get_facebook_images_url(img_links):
    urls = []

    for link in img_links:
        if link != "None":
            valid_url_found = False
            driver.get(link)

            try:
                while not valid_url_found:
                    WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located(
                            (By.CLASS_NAME, selectors.get("spotlight"))
                        )
                    )
                    element = driver.find_element_by_class_name(
                        selectors.get("spotlight")
                    )
                    img_url = element.get_attribute("src")

                    if img_url.find(".gif") == -1:
                        valid_url_found = True
                        urls.append(img_url)
            except Exception:
                urls.append("None")
        else:
            urls.append("None")

    return urls


# -------------------------------------------------------------
# -------------------------------------------------------------

# takes a url and downloads image from that url
def image_downloader(img_links, folder_name):
    img_names = []

    try:

        for link in img_links:
            img_name = "None"

            if link != "None":
                img_name = (link.split(".jpg")[0]).split("/")[-1] + ".jpg"

                # this is the image id when there's no profile pic
                if img_name == selectors.get("default_image"):
                    img_name = "None"
                else:
                    try:
                        urllib.request.urlretrieve(link, img_name)
                    except Exception:
                        img_name = "None"

            img_names.append(img_name)

    except Exception:
        print("Exception (image_downloader):", sys.exc_info()[0])

    return img_names


# -------------------------------------------------------------
# -------------------------------------------------------------


def check_height():
    new_height = driver.execute_script(selectors.get("height_script"))
    return new_height != old_height


# -------------------------------------------------------------
# -------------------------------------------------------------

# helper function: used to scroll the page
def scroll():
    global old_height
    current_scrolls = 0

    while True:
        try:
            if current_scrolls == total_scrolls:
                return

            old_height = driver.execute_script(selectors.get("height_script"))
            driver.execute_script(selectors.get("scroll_script"))
            WebDriverWait(driver, scroll_time, 0.05).until(
                lambda driver: check_height()
            )
            current_scrolls += 1
        except TimeoutException:
            break

    return


# -------------------------------------------------------------
# -------------------------------------------------------------

# --Helper Functions for Posts


def get_status(x):
    status = ""
    try:
        status = x.find_element_by_xpath(
            selectors.get("status")
        ).text  # use _1xnd for Pages
    except Exception:
        try:
            status = x.find_element_by_xpath(selectors.get("status_exc")).text
        except Exception:
            pass
    return status


def get_div_links(x, tag):
    try:
        temp = x.find_element_by_xpath(selectors.get("temp"))
        return temp.find_element_by_tag_name(tag)
    except Exception:
        return ""


def get_title_links(title):
    l = title.find_elements_by_tag_name("a")
    return l[-1].text, l[-1].get_attribute("href")


def get_title(x):
    title = ""
    try:
        title = x.find_element_by_xpath(selectors.get("title"))
    except Exception:
        try:
            title = x.find_element_by_xpath(selectors.get("title_exc1"))
        except Exception:
            try:
                title = x.find_element_by_xpath(selectors.get("title_exc2"))
            except Exception:
                pass
    finally:
        return title


def get_time(x):
    time = ""
    try:
        time = x.find_element_by_tag_name("abbr").get_attribute("title")
        time = (
            str("%02d" % int(time.split(", ")[1].split()[1]),)
            + "-"
            + str(
                (
                    "%02d"
                    % (
                        int(
                            (
                                list(calendar.month_abbr).index(
                                    time.split(", ")[1].split()[0][:3]
                                )
                            )
                        ),
                    )
                )
            )
            + "-"
            + time.split()[3]
            + " "
            + str("%02d" % int(time.split()[5].split(":")[0]))
            + ":"
            + str(time.split()[5].split(":")[1])
        )
    except Exception:
        pass

    finally:
        return time


def extract_and_write_posts(elements, filename):
    try:
        f = open(filename, "w", newline="\r\n")
        f.writelines(
            " TIME || TYPE  || TITLE || STATUS  ||   LINKS(Shared Posts/Shared Links etc) "
            + "\n"
            + "\n"
        )

        for x in elements:
            try:
                title = " "
                status = " "
                link = ""
                time = " "

                # time
                time = get_time(x)

                # title
                title = get_title(x)
                if title.text.find("shared a memory") != -1:
                    x = x.find_element_by_xpath(selectors.get("title_element"))
                    title = get_title(x)

                status = get_status(x)
                if (
                    title.text
                    == driver.find_element_by_id(selectors.get("title_text")).text
                ):
                    if status == "":
                        temp = get_div_links(x, "img")
                        if (
                            temp == ""
                        ):  # no image tag which means . it is not a life event
                            link = get_div_links(x, "a").get_attribute("href")
                            type = "status update without text"
                        else:
                            type = "life event"
                            link = get_div_links(x, "a").get_attribute("href")
                            status = get_div_links(x, "a").text
                    else:
                        type = "status update"
                        if get_div_links(x, "a") != "":
                            link = get_div_links(x, "a").get_attribute("href")

                elif title.text.find(" shared ") != -1:

                    x1, link = get_title_links(title)
                    type = "shared " + x1

                elif title.text.find(" at ") != -1 or title.text.find(" in ") != -1:
                    if title.text.find(" at ") != -1:
                        x1, link = get_title_links(title)
                        type = "check in"
                    elif title.text.find(" in ") != 1:
                        status = get_div_links(x, "a").text

                elif (
                    title.text.find(" added ") != -1 and title.text.find("photo") != -1
                ):
                    type = "added photo"
                    link = get_div_links(x, "a").get_attribute("href")

                elif (
                    title.text.find(" added ") != -1 and title.text.find("video") != -1
                ):
                    type = "added video"
                    link = get_div_links(x, "a").get_attribute("href")

                else:
                    type = "others"

                if not isinstance(title, str):
                    title = title.text

                status = status.replace("\n", " ")
                title = title.replace("\n", " ")

                line = (
                    str(time)
                    + " || "
                    + str(type)
                    + " || "
                    + str(title)
                    + " || "
                    + str(status)
                    + " || "
                    + str(link)
                    + "\n"
                )

                try:
                    f.writelines(line)
                except Exception:
                    print("Posts: Could not map encoded characters")
            except Exception:
                pass
        f.close()
    except Exception:
        print("Exception (extract_and_write_posts)", "Status =", sys.exc_info()[0])

    return


# -------------------------------------------------------------
# -------------------------------------------------------------


def save_to_file(name, elements, status, current_section):
    try:
        f = None  # file pointer
        if status != 4:
            f = open(name, "w", encoding="utf-8", newline="\r\n")

        results = []
        img_names = []

        # dealing with Photos
        if status == 1:
            results = [x.get_attribute("href") for x in elements]
            results.pop(0)

            try:
                if download_uploaded_photos:
                    if photos_small_size:
                        background_img_links = driver.find_elements_by_xpath(
                            selectors.get("background_img_links")
                        )
                        background_img_links = [
                            x.get_attribute("style") for x in background_img_links
                        ]
                        background_img_links = [
                            ((x.split("(")[1]).split(")")[0]).strip('"')
                            for x in background_img_links
                        ]
                    else:
                        background_img_links = get_facebook_images_url(results)

                    folder_names = ["Uploaded Photos", "Tagged Photos"]
                    #print("Downloading " + folder_names[current_section])

                    img_names = image_downloader(background_img_links,folder_names[current_section])
                else:
                    img_names = ["None"] * len(results)
            except Exception:
                print(
                    "Exception (Images)",
                    str(status),
                    "Status =",
                    current_section,
                    sys.exc_info()[0],
                )

        # dealing with Posts
        elif status == 4:
            extract_and_write_posts(elements, name)
            return

        """Write results to file"""
        if status == 1:
            for i, _ in enumerate(results):
                # image's link
                f.writelines(results[i])
                f.write(",")

                # downloaded picture id
                f.writelines(img_names[i])
                f.write("\n")

        elif status == 2:
            for x in results:
                f.writelines(x + "\n")

        f.close()

    except Exception:
        print("Exception (save_to_file)", "Status =", str(status), sys.exc_info()[0])

    return

# ----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def scrape_data(user_id, scan_list, section, elements_path, save_status, file_names):

    #os.chdir("./"+user_id.replace("https://www.facebook.com/",""))
    page = []

    if save_status == 4:
        page.append(user_id)

    page += [user_id + s for s in section]

    for i, _ in enumerate(scan_list):
        try:
            driver.get(page[i])

            if (
                (save_status == 0) or (save_status == 1) or (save_status == 2)
            ):  # Only run this for friends, photos and videos

                # the bar which contains all the sections
                sections_bar = driver.find_element_by_xpath(
                    selectors.get("sections_bar")
                )

                if sections_bar.text.find(scan_list[i]) == -1:
                    continue

            if save_status != 3:
                scroll()

            data = driver.find_elements_by_xpath(elements_path[i])

            save_to_file(file_names[i], data, save_status, i)

        except Exception:
            print(
                "Exception (scrape_data)",
                str(i),
                "Status =",
                str(save_status),
                sys.exc_info()[0],
            )


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def create_original_link(url):
    if url.find(".php") != -1:
        original_link = (
            facebook_https_prefix + facebook_link_body + ((url.split("="))[1])
        )

        if original_link.find("&") != -1:
            original_link = original_link.split("&")[0]

    elif url.find("fnr_t") != -1:
        original_link = (
            facebook_https_prefix
            + facebook_link_body
            + ((url.split("/"))[-1].split("?")[0])
        )
    elif url.find("_tab") != -1:
        original_link = (
            facebook_https_prefix
            + facebook_link_body
            + (url.split("?")[0]).split("/")[-1]
        )
    else:
        original_link = url

    return original_link

def scrap_profile(ids):
    # execute for all profiles given in input.txt file
    if 1==1:
        username=ids
        driver.get("https://www.facebook.com/"+ids)
        url = driver.current_url
        user_id = create_original_link(url)

        print("\nScraping:",ids)
        try:
            target_dir = "./{0}".format(username)
            os.chdir(target_dir)
        except Exception:
            print("Some error occurred in creating the profile directory.")


        print("Photos..")
        # setting parameters for scrape_data() to scrap photos
        scan_list = ["'s Photos", "Photos of"]
        section = ["/photos_all", "/photos_of"]
        elements_path = ["//*[contains(@id, 'pic_')]"] * 2
        file_names = ["Uploaded Photos.txt", "Tagged Photos.txt"]
        save_status = 1

        scrape_data(user_id, scan_list, section, elements_path, save_status, file_names)
        print("Photos Done!\n")

        print("Posts:")
        # setting parameters for scrape_data() to scrap posts
        scan_list = [None]
        section = []
        elements_path = ['//div[@class="_5pcb _4b0l _2q8l"]']

        file_names = ["Posts.txt"]
        save_status = 4

        scrape_data(user_id, scan_list, section, elements_path, save_status, file_names)
        print("Posts Done!")

    # ----------------------------------------------------------------------------

    print("\nProcess Completed.")
    os.chdir("../")

    return


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def safe_find_element_by_id(driver, elem_id):
    try:
        return driver.find_element_by_id(elem_id)
    except NoSuchElementException:
        return None


def login(email, password):
    """ Logging into our own profile """

    try:
        global driver
        fb_path = "https://www.facebook.com/"
        driver.get(fb_path)
        #driver.maximize_window()

        # filling the form
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("pass").send_keys(password)

        try:
            # clicking on login button
            driver.find_element_by_id("loginbutton").click()
        except NoSuchElementException:
            # Facebook new design
            driver.find_element_by_name("login").click()
        print("Login Successful")
    except Exception:
        print("There's some error in log in.")
        print(sys.exc_info()[0])
        exit(1)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def fbpost(user):
    #driver = webdriver.Firefox()
    with open("./social/credentials.yaml", "r") as ymlfile:
        cfg = yaml.safe_load(stream=ymlfile)

    if ("password" not in cfg) or ("email" not in cfg):
        print("Your email or password is missing. Kindly write them in credentials.txt")
        exit(1)

    if len(user) > 0:
        print("\nStarting Scraping...")

        login(cfg["email"], cfg["password"])
        scrap_profile(user)
        driver.close()
    else:
        print("Input file is empty.")
