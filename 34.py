import requests

link = "http://www.santostang.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
r = requests.get(link, headers=headers)
print(r.request.headers)
