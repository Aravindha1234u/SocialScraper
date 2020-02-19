import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from instagram_scraper import *
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white


def username(user):
    ch='y'
    while ch=="y" or ch=='Y':
        print(C+"1."+W+" Facebook "+C+"\n2."+W+" Twitter "+C+"\n3."+W+" Instagram")
        choice = input(C+"root@social_scraper:"+W+"~/Enter the Options: ")
        if choice == '1':
            Facebook(user)
        elif choice == '2':
            ScrapTweets(user)
            return()
        elif choice == '3':
            Instagram(user)
            return()
        ch=input(C+"Do you want to Continue again:"+W)
    exit()

def Facebook(user):

    print ( W + '[+]' + G + ' Fetching Data From Facebook...' + W +'\n')
    search_string = "https://en-gb.facebook.com/" + user

    #response is stored after request is made
    response = requests.get(search_string)

    #Response is stored and parsed to implement beautifulsoup
    soup = BeautifulSoup(response.text, 'html.parser')

    main_div = soup.div.find(id="globalContainer")

    def find_name():
        name = main_div.find(id="fb-timeline-cover-name").get_text()
        print("\n"+G+"Name:"+W+name)

    ###Finding About the user details
    #finding work details of the user
    def find_eduwork_details():
        education = soup.find(id="pagelet_eduwork")
        apple=education.find(attrs={"class":"_4qm1"})
        if (apple.get_text() != " "):
            for category in education.find_all(attrs={"class":"_4qm1"}):
                print(G+category.find('span').get_text() + " : "+W)
                for company in category.find_all(attrs={"class":"_2tdc"}):
                    if (company.get_text() != " "):
                        print(company.get_text())
                    else:
                        continue
        else:
            print("No work details found")

    #finding home details of the user
    def find_home_details():
        if(soup.find(id="pagelet_hometown") !=" "):
                home = soup.find(id="pagelet_hometown")
                for category in home.find_all(attrs={"class":"_4qm1"}):
                    print(G+category.find('span').get_text() + " : "+W)
                    for company in category.find_all(attrs={"class":"_42ef"}):
                        if (company.get_text() != " "):
                            print(company.get_text())
                        else:
                            continue
        else:
            print("No Home details found")

    #finding contact details of the user
    def find_contact_details():
        contact = soup.find(id="pagelet_contact")
        orange = contact.find(attrs={"class":"_4qm1"})
        if (orange.get_text() !=" "):
            for category in contact.find_all(attrs={"class":"_4qm1"}):
                print(G+category.find('span').get_text() + " : "+W)
                for company in category.find_all(attrs={"class":"_2iem"}):
                    if (company.get_text() != " "):
                        print(company.get_text())
                    else:
                        continue
        else:
             print("No Contact details found")
    if (not main_div.find(id="fb-timeline-cover-name")):
        print(R+"Error: Profile not found")
    elif ("200" in str(response)):
        find_name()
        find_eduwork_details()
        find_home_details()
    else:
        print(R+"Error: some other response")
    return()

def Instagram(user):
    print ('\n' + W + '[+]' + G + ' Fetching Data From Instagram...' + '\n')
    r = requests.get("https://www.instagram.com/"+ user +"/?__a=1")
    if r.status_code == 200:
        res = r.json()['graphql']['user']
        print(G+"\nUsername: " + W+res['username'])
        print(G+"Full Name: "+W+res['full_name'])
        try:
            print(G+"Business Category: "+W+res['edge_follow']['business_category_name'])
        except:
            print(G+"Account :"+W+" Private")
        finally:
            print(G+"Biograph: " + W+res['biography'])
            print(G+"URL: "+ W+str(res['external_url']))
            print(G+"Followers: "+W+str(res['edge_followed_by']['count']))
            print(G+"Following: "+W+str(res['edge_follow']['count']))
            print(G+"Profile Picture HD: " + W+res['profile_pic_url_hd'])
            scrape_insta(user)
    elif r.status_code == 404:
        print(R+"Error: Profile Not Found")
    else:
        print(R+"Error: Something Went Wrong")

def ScrapTweets(user):
    print (W + '[+]' + G + ' Fetching Data From Twitter...' + '\n')
    link = "https://twitter.com/" + user
    the_client = uReq(link)
    page_html = the_client.read()
    the_client.close()

    soup = BeautifulSoup(page_html, 'html.parser')

    try:
        full_name = soup.find('a', attrs={"class": "ProfileHeaderCard-nameLink u-textInheritColor js-nav"})
        print(G+"User Name --> " + W + str(full_name.text))
    except:
        print("User Name -->"+ R +" Not Found")
    print()

    try:
        user_id = soup.find('b', attrs={"class": "u-linkComplex-target"})
        print(G+"User Id --> "+W + str(user_id.text))
    except:
        print("User Id --> "+R+"Not Found")
    print()

    try:
        decription = soup.find('p', attrs={"class": "ProfileHeaderCard-bio u-dir"})
        print(G+"Description --> "+W + str(decription.text))
    except:
        print(R+"Decription not provided by the user")
    print()

    try:
        user_location = soup.find('span', attrs={"class": "ProfileHeaderCard-locationText u-dir"})
        print(G+"Location -->  " + W+ str(user_location.text.strip()))
    except:
        print(R+"Location not provided by the user")
    print()

    try:
        connectivity = soup.find('span', attrs={"class": "ProfileHeaderCard-urlText u-dir"})
        title = connectivity.a["title"]
        print(G+"Link provided by the user --> " +W+ str(title))
    except:
        print(R+"No contact link is provided by the user")
    print()

    try:
        join_date = soup.find('span', attrs={"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"})
        print(G+"The user joined twitter on --> " +W+ str(join_date.text))
    except:
        print(R+"The joined date is not provided by the user")
    print()

    try:
        birth = soup.find('span', attrs={"class": "ProfileHeaderCard-birthdateText u-dir"})
        birth_date = birth.span.text
        print(G+"Date of Birth:"+W+str(birth_date.strip()))
    except:
        print(R+"Birth Date not provided by the user")
    print()

    try:
        span_box = soup.findAll('span', attrs={"class": "ProfileNav-value"})
        print(G+"Total tweets --> " + W+span_box[0].text)
    except:
        print(R+"Total Tweets --> Zero")
    print()

    try:
        print(G+"Following --> " +W+span_box[1].text)
    except:
        print(R+"Following --> Zero")
    print()

    try:
        print(G+"Followers --> " +W+ span_box[2].text)
    except:
        print(R+"Followers --> Zero")
    print()

    try:
        print(G+"Likes send by him --> " + W+span_box[3].text)
    except:
        print(R"Likes send by him --> Zero")
    print()

    try:
        if span_box[4].text != "More ":
            print(G+"No. of parties he is Subscribed to --> " + W+span_box[4].text)
        else:
            print(G+"No. of parties he is Subscribed to --> Zero")
    except:
        print("No. of parties he is Subscribed to --> Zero")
    print(W)

    spana = soup.findAll('span', attrs={"class": "ProfileNav-value"})

    print(G+"Tweets by "+W+ str(username) + " are --> ")
    # TweetTextSize TweetTextSize--normal js-tweet-text tweet-text
    for tweets in soup.findAll('p', attrs={"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
        print(tweets.text)
        print()
