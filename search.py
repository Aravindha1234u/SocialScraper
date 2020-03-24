import requests
from social.api import google
import os

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def search():
    f=open("user.txt","r")
    username=[j for i in f for j in i.split()]
    f.close()
    for user in username:
        acc=[]
        r=requests.get("https://www.googleapis.com/customsearch/v1?key="+google()+"&q="+user)
        if r.status_code==200:
            try:
                os.mkdir(user)
            except:
                pass
            f1=open("./{0}/{1}.txt".format(user,user),"w+")
            f1.write("\n")
            res = r.json()
            print("\n")
            #print(res)
            print(C+"Found Account At \n")
            for i in res['items']:
                if i["displayLink"] not in acc:
                    acc.append(str(i["displayLink"]))
                    for j in i.keys():
                        if j=="displayLink":
                            print(W+str(i[j]))
                        else:
                            pass
                        f1.write(j+" : "+str(i[j]))
                        f1.write("\n")
                else:
                    pass
                f1.write("\n")
            f1.close()
            print()
            print("Fetched Details are Solved at "+"./{0}/{1}.txt".format(user,user))
            if input("Do you want to open it (Y/N):") in ("Y","y"):
                os.system("cat "+"./{0}/{1}.txt".format(user,user))
            acc.clear()
        else:
            print(R+"Error : " + str(r.status_code))
    return
