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
    user=[]
    print(C+"1."+W+"Single Username")
    print(C+"2."+W+"Multiple Username As File")
    ch=int(input(C+"Enter the choice:"+W))
    if ch==1:
        user.append(input("\nEnter the username:"))
    else:
        filename=input("Filename with Directory:")
        try:
            f=open(filename,"r")
            s=f.read()
            user=s.split()
            f.close()
        except:
            print(R+"File not Found")
            username()
    ch='y'
    while ch=="y" or ch=='Y':
        print(C+"1."+W+" Instagram "+C+"\n2."+W+" Twitter "+C+"\n3."+W+" Facebook ")
        choice = input(C+"root@social_scraper:"+"~/Enter the Options: "+W)
        if choice == '1':
            for i in user:
                Instagram(i)
        elif choice == '2':
            for i in user:
                ScrapTweets(i)
            return()
        elif choice == '3':
            for i in user:
                Facebook(i)
            return()
        ch=input(C+"\n\nDo you want to Continue again:"+W)

    exit()
