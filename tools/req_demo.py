import requests

url1 = "https://www.aliyun.com"

url2 = "https://fecs.console.aliyun.com/data/api.json"

headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36' }

data1 = {
    "product" : "aliyun_aiassistant",
    "action" : "ListSession",
}

par = {
    "fetcher": "aliyun_aiassistant__ListSession"
}


def getsend():
    r = requests.get(url1,headers=headers)
    print(r.content)

def postsendform():
    r = requests.post(url2,headers=headers,params=par,data=data1)
    print(r.content)

def postsendjson():
    r = requests.post(url2,headers=headers,params=par,json=data1)
    print(r.content)

if __name__ == "__main__":
    getsend()
    postsendjson()
    postsendform()