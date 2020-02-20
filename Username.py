import requests
from bs4 import BeautifulSoup
from social.instagram import Instagram
from social.facebook import Facebook
from social.twitter import ScrapTweets

import os
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def username():
    f=open("user.txt","r")
    user=[j for i in f for j in i.split()]
    ch='y'
    while ch=="y" or ch=='Y':
        print(C+"1."+W+" Facebook "+C+"\n2."+W+" Twitter "+C+"\n3."+W+" Instagram")
        choice = input(C+"root@social_scraper:"+"~/Enter the Options: "+W)
        if choice == '1':
            for i in user:
                Facebook(i)
        elif choice == '2':
            for i in user:
                ScrapTweets(i)
            return()
        elif choice == '3':
            for i in user:
                Instagram(i)
            return()
        ch=input(C+"Do you want to Continue again:"+W)
    f.close()
    exit()
