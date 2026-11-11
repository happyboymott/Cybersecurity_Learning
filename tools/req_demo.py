import requests

url = "https://caigamer.cn/"

headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0' }

data1 = {
    "username" : "admin",
    "password" : "1111",
    "login" : "login"
}

par = {
    "login": "true"
}

proxie = {
    "http" : "127.0.0.1:8080",
    "https" : "127.0.0.1:8080"
}


def getsend():
    r = requests.get(url,headers=headers,proxies=proxie,verify=False)
    print(r.content)

def postsendform():
    r = requests.post(url,headers=headers,params=par,data=data1,proxies=proxie,verify=False)
    print(r.content)

def postsendjson():
    r = requests.post(url,headers=headers,params=par,json=data1,proxies=proxie,verify=False)
    print(r.content)

if __name__ == "__main__":
    getsend()
    postsendjson()
    postsendform()