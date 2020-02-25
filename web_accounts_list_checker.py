import requests
import json

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def checkuser():
    f = open("web.json","r")
    data = json.load(f)
    f.close()
    f=open("user.txt","r")
    user=[j for i in f for j in i.split()]
    f.close()
    print()
    for user_id in user:
        print (W + '[+]' + G + ' Fetching Data of {} using Web Crawler...'.format(user)+W)
        for i in data['sites']:
            #print(i['name'])
            r = requests.get(i['check_uri'].replace("{account}",user_id))
            if r.status_code == 200:
                print(i['name'])
checkuser()
