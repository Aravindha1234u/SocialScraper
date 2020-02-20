from igql import InstagramGraphQL
import urllib.request
import ast
import os
from image import *
import re
from social.instagram import Instagram


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def scrape_insta(user):
    confidence=[]
    percent=[]
    predator=[]
    username1=user
    f=open('wordlist.txt','r')
    wordlist=[]
    for i in f:
        for j in i.split():
            wordlist.append(j)
    f.close()
    try:
        os.mkdir(user)
    except:
        print()
    f1=open("./{0}/{1}.txt".format(user,user),"w+")
    igql_api = InstagramGraphQL()
    user = igql_api.get_user(user)
    print()
    for media in user.timeline():
        for i in media:
            f1.write("\nID: "+i['node']["id"])
            try:
                f1.write("\nCaption: "+ str(i["node"]["edge_media_to_caption"]["edges"][0]['node']['text']))
            except:
                f1.write("")
            else:
                f1.write("\nCaption:")
            f1.write("\nShortCode:"+i['node']["shortcode"])
            f1.write("\nComment:"+ str(i['node']["edge_media_to_comment"]['count']))
            media1 = igql_api.get_media(i['node']["shortcode"])
            comments = []
            for comments_batch in media1.comments():
                comments.append(comments_batch)
            for comments_batch in comments[0]:
                j1 = ast.literal_eval(str(comments_batch['node']))
                f1.write("\nOwner:"+j1['owner']['username'])
                f1.write("\nText:"+j1['text'])
                if j1['text'] in wordlist:
                    print(R+"{} May be a Predator".format(j1['owner']['username'])+W)
                    confidence.append(int(10))
                    predator.append(j1['owner']['username'])
            f1.write("\nTimestamp:"+ str(i['node']["taken_at_timestamp"]))
            f1.write("\nDimensions:"+str(i['node']["dimensions"]['height'])+" X "+str(i['node']["dimensions"]['width']))
            f1.write("\nURL:"+str(i['node']["display_url"]))
            urllib.request.urlretrieve(str(i['node']["display_url"]),str(username1)+"/"+i['node']["id"]+".jpg")
            f1.write("\nLikes:"+str(i['node']["edge_liked_by"]['count']))
            f1.write("\nLocation:"+str(i['node']["location"]))
            f1.write("\nOwner:"+str(i['node']["owner"]["username"]))
            f1.write("accessibility_caption:"+str(i['node']["accessibility_caption"]))
            if str(i['node']["accessibility_caption"]) in wordlist:
                f1.write(R+"Image may Contain Insecure Content")

    print("\nPredator Identity Details:\n")
    if len(predator)>0:
        for i in predator:
            Instagram(i)
            arr=os.listdir("./{}".format(str(i)))
            for j in arr:
                if re.match(r".+\.jpg",j):
                    confidence[predator.index(i)]+=imageai("./{}".format(str(i))+"/"+j)
                    print(confidence[predator.index(i)])
    else:
        return
    f1.close()
