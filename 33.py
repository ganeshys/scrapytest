import requests

r = requests.get('http://www.santostang.com')
print(r.request.headers)
