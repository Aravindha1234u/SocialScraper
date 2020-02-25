import requests
from api import api_key,api_secret

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
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    data=r.json()

    for i in data['output']['detections']:
        for j in i.keys():
            if str(j)=="confidence" and float(i[j])*100 > 75:
                print(R+str(j)+" : "+str(float(i[j])*100)+"%")
                nsfw(url)
            elif str(j)=="confidence" and float(i[j])*100 > 50:
                print(C+str(j)+" : "+str(float(i[j])*100)+"%")
            elif str(j)=="confidence" and float(i[j])*100 > 35:
                print(G+str(j)+" : "+str(float(i[j])*100)+"%")
            else:
                print(W+str(j)+" : "+str(i[j]))
        print()
def imageai(url):
    #imagga api
    key = api_key()
    secret = api_secret()

    r = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(key, secret),
        files={'image': open(url, 'rb')})
    data=r.json()
    #exit()
    for i in data['result']['tags']:
        for j in i.keys():
            if str(j)=="confidence" and float(i[j]) > 75:
                print(R+str(j)+" : "+str(float(i[j]))+"%")
                #nsfw(url)
            elif str(j)=="confidence" and float(i[j]) > 50:
                print(C+str(j)+" : "+str(float(i[j]))+"%")
            elif str(j)=="confidence" and float(i[j]) > 35:
                print(G+str(j)+" : "+str(float(i[j]))+"%")
            else:
                print(W+str(j)+" : "+str(i[j]))
        print()
#imageai("/root/Downloads/SocialScraper/image.jpeg")
