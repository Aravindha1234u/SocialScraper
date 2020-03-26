import requests
from bs4 import BeautifulSoup
import os

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def Facebook(user):

    print ( W + '[+]' + G + ' Fetching Data From Facebook...' + W +'\n')
    search_string = "https://en-gb.facebook.com/" + user

    #response is stored after request is made
    response = requests.get(search_string)

    #Response is stored and parsed to implement beautifulsoup
    soup = BeautifulSoup(response.text, 'html.parser')

    if ("404" in str(response)):
        print(R+"Error: Profile not found")
    elif ("200" in str(response)):
        try:
            os.mkdir(user)
        except:
            pass
        f1=open("./{0}/{1}.txt".format(user,user),"w+")
        main_div = soup.div.find(id="globalContainer")

        name = main_div.find(id="fb-timeline-cover-name").get_text()
        f1.write("\n"+"Name:"+name)
        f1.write("\n")
        ###Finding About the user details
        #finding work details of the user

        education = soup.find(id="pagelet_eduwork")
        apple=education.find(attrs={"class":"_4qm1"})
        if (apple.get_text() != " "):
            for category in education.find_all(attrs={"class":"_4qm1"}):
                f1.write(category.find('span').get_text() + " : "+W)
                for company in category.find_all(attrs={"class":"_2tdc"}):
                    if (company.get_text() != " "):
                        f1.write(company.get_text())
                        f1.write("\n")
                    else:
                        continue
        else:
            f1.write("No work details found")
            f1.write("\n")

        #finding home details of the user
        if(soup.find(id="pagelet_hometown") !=" "):
                home = soup.find(id="pagelet_hometown")
                for category in home.find_all(attrs={"class":"_4qm1"}):
                    f1.write(category.find('span').get_text() + " : "+W)
                    for company in category.find_all(attrs={"class":"_42ef"}):
                        if (company.get_text() != " "):
                            f1.write(company.get_text())
                            f1.write("\n")
                        else:
                            continue
        else:
            f1.write("No Home details found")
            f1.write("\n")
        #finding contact details of the user
        contact = soup.find(id="pagelet_contact")
        orange = contact.find(attrs={"class":"_4qm1"})
        if (orange.get_text() !=" "):
            for category in contact.find_all(attrs={"class":"_4qm1"}):
                f1.write(category.find('span').get_text() + " : "+W)
                for company in category.find_all(attrs={"class":"_2iem"}):
                    if (company.get_text() != " "):
                        f1.write(company.get_text())
                        f1.write("\n")
                    else:
                        continue
        else:
             f1.write("No Contact details found")
             f1.write("\n")
        f1.close()
    else:
        print(R+"Error: some other response")
    return()
