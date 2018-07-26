import re

line = "Fat cats are smarter than dogs, is it right?"
m = re.match(r'(.*) are (.*?) dogs', line)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())
