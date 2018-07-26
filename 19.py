import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
for i in range(1, 11):
    link = "https://hz.fang.anjuke.com/loupan/all/p" + str(i) + "/"
    r = requests.get(link, headers)
    print('现在爬取的是第', i, '页')
    soup = BeautifulSoup(r.text, 'lxml')
    house_list = soup.find_all('div', class_='infos')
    for house in house_list:
        name = house.find('span', class_='items-name').text.strip()

        print(name)
        time.sleep(5)
