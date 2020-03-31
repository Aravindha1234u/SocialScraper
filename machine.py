import requests

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def machine(user):
    r = requests.post(
        "https://api.deepai.org/api/sentiment-analysis",
        files={
            'text': open("./"+str(user)+"/"+str(user)+".txt", 'rb'),
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        )
    data = r.json()
    
    if 'Negative' in data['output']:
        print(R+"{} May be a Predator".format(user)+W)
        return True
    else:
        return False
