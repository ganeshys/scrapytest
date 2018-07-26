# 超时异常
import requests

link = "http://www.santostang.com"
r = requests.get(link, timeout=0.00001)
