import requests
from bs4 import BeautifulSoup

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

    main_div = soup.div.find(id="globalContainer")

    def find_name():
        name = main_div.find(id="fb-timeline-cover-name").get_text()
        print("\n"+"Name:"+name)

    ###Finding About the user details
    #finding work details of the user
    def find_eduwork_details():
        education = soup.find(id="pagelet_eduwork")
        apple=education.find(attrs={"class":"_4qm1"})
        if (apple.get_text() != " "):
            for category in education.find_all(attrs={"class":"_4qm1"}):
                print(category.find('span').get_text() + " : "+W)
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
                    print(category.find('span').get_text() + " : "+W)
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
                print(category.find('span').get_text() + " : "+W)
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
