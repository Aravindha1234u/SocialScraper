import requests
import webbrowser

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def reverseimagesearch():
    try:
        img=input(W+"Enter the image path:")
        surl='https://www.google.co.in/searchbyimage/upload'
        print (W + '[+]' + G + ' Searching...'+W)
        murl={'encoded_image': (img, open(img, 'rb')), 'image_content': ''}
        response = requests.post(surl, files=murl, allow_redirects=False)
        fetchUrl = response.headers['Location']
        openWeb = input(C+"Open Search Result in web broser? (Y/N) : "+W)
        if openWeb.upper() == 'Y':
            webbrowser.open(fetchUrl)
        else:
            pass
    except IOError:
        print()
        print(R+"ERROR : File Does not Exist\n")
        reverseimagesearch()
