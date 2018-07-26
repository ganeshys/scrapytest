import requests
from bs4 import BeautifulSoup

url = "http://www.w3school.com.cn/"
r = requests.get(url)
r.encoding = 'gb2312'
suop = BeautifulSoup(r.text, "lxml")
res = suop.find('div', id='d1').h2.text
print(res)
