from igql import InstagramGraphQL
import urllib.request
import ast
import os

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def scrape_insta(user):
    username1=user
    predator=[]
    os.mkdir(str(username1))
    f=open('wordlist.txt','r')
    wordlist=[]
    for i in f:
        for j in i.split():
            wordlist.append(j)
    igql_api = InstagramGraphQL()
    user = igql_api.get_user(user)
    print()
    for media in user.timeline():
        for i in media:
            #print(i['node'].keys())
            print("ID: "+i['node']["id"])
            try:
                print("Caption: "+ str(i["node"]["edge_media_to_caption"]["edges"][0]['node']['text']))
            except:
                print("")
            else:
                print("Caption:")
            print("ShortCode:"+i['node']["shortcode"])
            print("Comment:"+ str(i['node']["edge_media_to_comment"]['count']))
            media1 = igql_api.get_media(i['node']["shortcode"])
            comments = []
            print()
            for comments_batch in media1.comments():
                comments.append(comments_batch)
            for comments_batch in comments[0]:
                j1 = ast.literal_eval(str(comments_batch['node']))
                print("Owner:"+j1['owner']['username'])
                print("Text:"+j1['text'])
                if j1['text'] in wordlist:
                    print(R+"{} May be a Predator".format(j1['owner']['username'])+W)
                    predator.append(j1['owner']['username'])
                print()
            print("Timestamp:"+ str(i['node']["taken_at_timestamp"]))
            print("Dimensions:"+str(i['node']["dimensions"]['height'])+" X "+str(i['node']["dimensions"]['width']))
            print("URL:"+str(i['node']["display_url"]))
            urllib.request.urlretrieve(str(i['node']["display_url"]),str(username1)+"/"+i['node']["id"]+".jpg")
            print("Likes:"+str(i['node']["edge_liked_by"]['count']))
            print("Location:"+str(i['node']["location"]))
            print("Owner:"+str(i['node']["owner"]["username"]))
            print("accessibility_caption:"+str(i['node']["accessibility_caption"]))
            if str(i['node']["accessibility_caption"]) in wordlist:
                print(R+"Image may Contain Insecure Content")
            print()
    print("\nPredator Identity Details:\n")
    for i in predator:
        print("Predator "+str(int(predator.index(i))+1)+": "+str(i)+"\n")
