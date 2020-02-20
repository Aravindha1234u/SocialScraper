from Username import *
from title import *

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def main():
    while True:
        ch='y'
        title()
        print(C+"1."+W+"Check in Social Media")
        print(C+"2."+W+"Platforms and Website")
        ch=input(C+"root@social_scraper:~/Username#"+C+"Enter the choice:"+W)
        if ch=='1':
            username()
        elif ch=='2':
            #checkuser(user)
            return
        else:
            print("Invalid Choice")

        ch=input("Do you want to Continue(Y/N):")
        if ch=='y' or ch=='Y':
            continue
        else:
            print("\nThank You")
            break

if __name__ == '__main__':
    main()
