#!　/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
import sys

url = 'https://news.yahoo.co.jp'
res = requests.get(url)
print(res.text[:500])

soup = BeautifulSoup(res.text, "html.parser")

elems = soup.find_all("a")
print(elems)

elems2 = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
print(elems2)

for elem in elems2:
    print(elem.contents[0])
    print(elem.attrs['href'])