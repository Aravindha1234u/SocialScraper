import requests

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def Instagram(user):
    print ('\n' + W + '[+]' + G + ' Fetching Data From Instagram...' + '\n')
    try:
        os.mkdir("../"+user)
    except:
        print()
    f1=open("../{0}/{1}.txt".format(user,user),"w+")
    r = requests.get("https://www.instagram.com/"+ user +"/?__a=1")
    if r.status_code == 200:
        res = r.json()['graphql']['user']
        f1.write("Username: "+res['username'])
        f1.write("\nFull Name: "+res['full_name'])
        try:
            f1.write("\nBusiness Category: "+res['edge_follow']['business_category_name'])
        except:
            f1.write("\nAccount :"+"Public")
        else:
            f1.write("\nAccount :"+" Private")
        finally:
            f1.write("\nBiograph: " + res['biography'])
            f1.write("\nURL: "+ str(res['external_url']))
            f1.write("\nFollowers: "+str(res['edge_followed_by']['count']))
            f1.write("\nFollowing: "+str(res['edge_follow']['count']))
            f1.write("\nProfile Picture HD: " + res['profile_pic_url_hd']+"\n")
    elif r.status_code == 404:
        print(R+"Error: Profile Not Found")
        exit()
    else:
        print(R+"Error: Something Went Wrong")
        exit()
    f1.close()
