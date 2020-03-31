import requests
from social.api import google
import os

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def search():
    print(C+"1."+W+"Single Username")
    print(C+"2."+W+"Multiple Username As File")
    ch=int(input(C+"Enter the choice:"+W))
    username=[]
    if ch==1:
        username.append(input("Enter the Username: "))
        pass
    elif ch==2:
        filename=input("Filename with Directory:")
        try:
            f=open(filename,"r")
            s=f.read()
            user=s.split()
            f.close()
        except:
            print(R+"File not Found")
            search()
    else:
        print("Invalid Choice")
        return

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
            print (W + '[+]' + G + ' Fetching Osint Reconnaissance...'+W)
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
