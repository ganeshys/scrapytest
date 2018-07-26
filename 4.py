import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Host': 'http://www.santostang.com/'
}
r = requests.get('http://www.santostang.com/', headers=headers)
print("响应状态码", r.status_code)
