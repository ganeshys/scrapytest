import requests
from bs4 import BeautifulSoup
import time
import random

link = "http://www.santostang.com/"


def scrapy(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    r = requests.get(link, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    return soup


soup = scrapy(link)
title_list = soup.find_all("h1", class_="post-title")

for eachone in title_list:
    url = eachone.a['href']
    print('开始爬去这篇博客:', url)
    soup_article = scrapy(url)
    title = soup_article.find("h1", class_="view-title").text.strip()
    print('这篇博客的标题为:', title)
    sleep_time = random.randint(0, 2) + random.random()
    print('开始休息', sleep_time, '秒')
    time.sleep(sleep_time)
