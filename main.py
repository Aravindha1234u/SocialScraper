from Username import *
from title import *

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def main():
    title()
    user=input(C+"root@social_scraper:"+W+"~/Username# Enter the Username:")
    username(user)
if __name__ == '__main__':
    main()
