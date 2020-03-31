import requests
try:
    from api import *
except:
    from .api import *

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def nsfw(url):
    #deepai api

    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            'image': open(url, 'rb'),
        },
        headers={'api-key': deepai()}
    )
    data=r.json()


    #data={'output':{'detections':[{'confidence' : '0.7077', 'tag' : {'en': 'bikini'}},{'confidence' : '0.8091878890991','tag' : {'en': 'summer'}}]}}

    confidence=[]
    for i in data['output']['detections']:
        for j in i.keys():
            if str(j)=="confidence" and float(i[j])*100 > 75:
                print(R+str(j)+" : "+str(float(i[j])*100)+"%")
                confidence.append(float(i[j])*100)
            elif str(j)=="confidence" and float(i[j])*100 > 50:
                print(C+str(j)+" : "+str(float(i[j])*100)+"%")
                confidence.append(float(i[j])*100)
            elif str(j)=="confidence" and float(i[j])*100 > 35:
                print(G+str(j)+" : "+str(float(i[j])*100)+"%")
                confidence.append(float(i[j])*100)
            else:
                print(W+str(j)+" : "+str(i[j]))
    print()
    for i in confidence:
        if i>=90:
            return True
def imageai(url):
    print("Media Processing......")

    #imagga api
    key = api_key()
    secret = api_secret()

    r = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(key, secret),
        files={'image': open(url, 'rb')})
    data=r.json()


    #data={'result':{'tags':[{'confidence' : '70.77', 'tag' : {'en': 'bikini'}},{'confidence' : '7.08091878890991','tag' : {'en': 'summer'}}]}}

    f=open('wordlist.txt','r')
    wordlist=[]
    for i in f:
        for j in i.split():
            wordlist.append(j)
    f.close()
    tags=[]
    print()
    for i in data['result']['tags'][:5]:
        for j in i.keys():
            if str(j)=="confidence" and float(i[j]) > 75:
                print(R+str(j)+" : "+str(float(i[j]))+"%")
                #nsfw(url)
            elif str(j)=="confidence" and float(i[j]) > 50:
                print(C+str(j)+" : "+str(float(i[j]))+"%")
            elif str(j)=="confidence" and float(i[j]) > 35:
                print(G+str(j)+" : "+str(float(i[j]))+"%")
            else:
                if str(type(i[j])) == "<class 'dict'>":
                    print(W+str(j)+" : "+str(i[j]['en']))
            if str(j)!="confidence":
                tags.append(str(i[j]['en']))
    print()
    for i in tags:
        for j in wordlist:
            if i==j:
                n=1
                break
    if n==1:
        print("Checking for NSFW")
        print()
        if nsfw(url):
            print("Resolving....")
            return True
    else:
        return False
