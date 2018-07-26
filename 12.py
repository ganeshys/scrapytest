import re

m = re.match('www', 'www.santostang.com')
print("匹配的结果:", m)
print("匹配的起始和终点:", m.span())
print("匹配的起始位置:", m.start())
print("匹配的终点位置", m.end())
