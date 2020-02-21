import requests

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def imageai(url):
    '''
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            'image': open(url, 'rb'),
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    data=r.json()'''
    data={'output': {'detections': [{'confidence': '0.97', 'bounding_box': [186, 629, 309, 304], 'name': 'Female Breast - Exposed'}, {'confidence': '0.97', 'bounding_box': [461, 442, 256, 258], 'name': 'Female Breast - Exposed'}], 'nsfw_score': 0.9958459734916687}, 'id': '9ead193a-067b-4f83-8f6a-9fe5ee1ff05d'}
    for i in data['output']['detections']:
        for j in i.keys():
            if str(j)=="confidence" and float(i[j])*100 > 75:
                print(R+str(j)+" : "+str(float(i[j])*100)+"%")
            elif str(j)=="confidence" and float(i[j])*100 > 50:
                print(C+str(j)+" : "+str(float(i[j])*100)+"%")
            elif str(j)=="confidence" and float(i[j])*100 > 35:
                print(G+str(j)+" : "+str(float(i[j])*100)+"%")
            else:
                print(W+str(j)+" : "+str(i[j]))
        print()
