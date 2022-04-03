#!　/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
import sys
import urllib.request
from urllib.parse import quote
import time

keyword = 'JAL ニュース'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"

def get_search_html(keyword, page):
    start = "&start=" + str(page * 10) # 次ページstart=10
    url = 'https://www.google.com/search?q=' + quote(keyword) + start 
    
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as res:
        body = res.read()
        return body


max_page = 5

for page in range(max_page):
    html = get_search_html(keyword, page)
    soup = BeautifulSoup(html, 'html.parser')

    elemg = soup.select('div.yuRUbf > a ')
    elemori = soup.select('div.yuRUbf > a > h3')
    #URL
    print(elemg[1].attrs['href'])
    
    #title
    print(elemori[1])
    # for elem in elems:
    #     print(elem.contents[0])
        # print(elem.attrs['href'])
    
    
    # title_text = soup.find('title').get_text()
    # print(title_text)

    time.sleep(3) # アクセス制限対策
    