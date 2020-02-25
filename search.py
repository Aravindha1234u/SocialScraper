import requests
def search():
    r=requests.get("https://serpapi.com/search?engine=google&q=Coffee")
    if r.status_code==200:
        res = r.json()
        for i in res.keys():
            try:
                for j in res[i].keys():
                    print(j+" : "+str(res[i][j]))
                    exit()
            except:
                pass
search()
