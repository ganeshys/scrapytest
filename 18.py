import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
link = 'https://beijing.anjuke.com/sale/'
r = requests.get(link, headers)

soup = BeautifulSoup(r.text, 'lxml')
house_list = soup.find_all('li', class_="list-item")

for house in house_list:
    name = house.find('div', class_='house-title').a.text.strip()
    price = house.find('span', class_='price-det').text.strip()

print(name, price)
