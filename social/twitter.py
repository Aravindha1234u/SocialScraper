import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import urllib.request
import re
import os
import json
from bs2json import bs2json
import pprint
from social.mail import *
from social.image import *
from machine import *

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def ScrapTweets(user):
    print ('[+]' + G + ' Fetching Data {} From Twitter...'.format(user) + '\n'+W)
    link = "https://twitter.com/" + user
    r=requests.get(link)
    if r.status_code == 200:
        the_client = uReq(link)
        page_html = the_client.read()
        the_client.close()
        f=open('wordlist.txt','r')
        wordlist=[]
        predator=[]
        for i in f:
            for j in i.split():
                wordlist.append(j)
        f.close()
        soup = BeautifulSoup(page_html, 'html.parser')
        try:
            os.mkdir(user)
        except:
            pass
        f1=open("./{0}/{1}.txt".format(user,user),"w+")

        try:
            full_name = soup.find('a', attrs={"class": "ProfileHeaderCard-nameLink u-textInheritColor js-nav"})
            f1.write("\nUser Name : " + str(full_name.text))
        except:
            f1.write("\nUser Name -->"+ R +" Not Found")

        try:
            user_id = soup.find('b', attrs={"class": "u-linkComplex-target"})
            f1.write("\nUser Id : "+str(user_id.text))
        except:
            f1.write("\nUser Id : "+"Not Found")

        try:
            decription = soup.find('p', attrs={"class": "ProfileHeaderCard-bio u-dir"})
            f1.write("\nDescription : "+str(decription.text))
        except:
            f1.write("\nDecription not provided by the user")

        try:
            user_location = soup.find('span', attrs={"class": "ProfileHeaderCard-locationText u-dir"})
            f1.write("\nLocation :  " +  str(user_location.text.strip()))
        except:
            f1.write("\nLocation not provided by the user")

        try:
            connectivity = soup.find('span', attrs={"class": "ProfileHeaderCard-urlText u-dir"})
            title = connectivity.a["title"]
            f1.write("\nLink provided by the user : " + str(title))
        except:
            f1.write("\nNo contact link is provided by the user")

        try:
            join_date = soup.find('span', attrs={"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"})
            f1.write("\nThe user joined twitter on : " + str(join_date.text))
        except:
            f1.write("\nThe joined date is not provided by the user")

        try:
            birth = soup.find('span', attrs={"class": "ProfileHeaderCard-birthdateText u-dir"})
            birth_date = birth.span.text
            f1.write("\nDate of Birth:"+str(birth_date.strip()))
        except:
            f1.write("\nBirth Date not provided by the user")

        try:
            span_box = soup.findAll('span', attrs={"class": "ProfileNav-value"})
            f1.write("\nTotal tweets : " + span_box[0].text)
        except:
            f1.write("\nTotal Tweets : Zero")

        try:
            f1.write("\nFollowing : " +span_box[1].text)
        except:
            f1.write("\nFollowing : Zero")

        try:
            f1.write("\nFollowers : " + span_box[2].text)
        except:
            f1.write("\nFollowers : Zero")

        try:
            f1.write("\nLikes send by him : " + span_box[3].text)
        except:
            f1.write("\nLikes send by him : Zero")

        try:
            if span_box[4].text != "More ":
                f1.write("\nNo. of parties he is Subscribed to : " + span_box[4].text)
            else:
                f1.write("\nNo. of parties he is Subscribed to : Zero")
        except:
            f1.write("\nNo. of parties he is Subscribed to : Zero")
        f1.write(W)

        spana = soup.findAll('span', attrs={"class": "ProfileNav-value"})

        f1.write("\nTweets by "+ str(user) + " are : ")

        for tweets in soup.findAll('p', attrs={"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
            tweets=bs2json().convert(tweets)
            try:
                f1.write(tweets['p']['text'])
                f1.write("\n")
            except:
                pass
            '''
            for i in range(len(tweets['p']['a'])-1,len(tweets['p']['a'])):
                try:
                    #print("http://"+str(tweets['p']['a'][i]['text']))
                    response = requests.get("http://"+tweets['p']['a'][i]['text'])
                    soup = BeautifulSoup(response.text, 'html.parser')
                    img_tags = soup.find_all('img')
                    s=str(img_tags).split()
                    print(s)
                    quit()
                except:
                    pass
            continue
            '''
            for i in range(0,len(tweets['p']['a'])):
                try:
                    f1.write(str(tweets['p']['a'][i]['s']['text'])+str(tweets['p']['a'][i]['b']['text']))
                    f1.write("\n")
                    if str(tweets['p']['a'][i]['b']['text']) in wordlist:
                        predator.append(user)
                        print(R+"{} May be a Predator".format(user)+W)
                except KeyError as e:
                    try:
                        if str(tweets['p']['a'][i]['text']).split()!=[]:
                            f1.write(tweets['p']['a'][i]['text'])
                            f1.write("\n")
                            response = requests.get("http://"+tweets['p']['a'][i]['text'])
                            soup = BeautifulSoup(response.text, 'html.parser')
                            img_tags = soup.find_all('img')
                            s=str(img_tags).split()
                            media=[]
                            for i in s:
                            	if "/media/" in i:
                            		media.append(i)
                            regex=r'https?:\/\/.*\.(?:png|jpg)'
                            for i in media:
                                matches=re.findall(regex,i)[0]
                                urllib.request.urlretrieve(matches,str(user)+"/"+str(matches[-19:]))
                        else:
                            pass
                    except KeyError as e:
                        pass
                else:
                    pass
            f1.write("\n")
        f1.close()
        print("Fetched Details are Saved at "+"./{0}/{1}.txt".format(user,user))
        if len(predator)>0:
            print(R+"\nPredator Identity Details:\n")
            for i in predator:
                ScrapTweets(i)
                arr=os.listdir("./{}".format(str(i)))
                for j in arr:
                    if re.match(r".+\.jpg",j):
                        if imageai("./{}".format(str(i))+"/"+j) == True:
                            print(R+"{} Is a Predator".format(str(i))+W)
            print("Fetched Details are Saved at "+"./{0}/{1}.txt".format(str(i),str(i)))
            for i in predator:
                print("./{0}/{1}.txt".format(i,i))
                f=open("./{0}/{1}.txt".format(i,i),'r')
                message=f.read()
                f.close()

                #AutoMail Generated
                mail(message)
        else:
            print(R+"\nUser Profile Details:\n"+W)
            print("Fetched Details are Saved at "+"./{0}/{1}.txt".format(user,user))
            f=open("./{0}/{1}.txt".format(user,user),'r')
            f.seek(0)
            message=f.read()
            f.close()

            #AutoMail Generated
            mail(message)
    elif r.status_code == 404:
        print(R+"Error: Profile Not Found")
        exit()
    else:
        print(R+"Error: Something Went Wrong")
        exit()
