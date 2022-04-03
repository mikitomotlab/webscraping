#!　/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
import sys
import urllib.request
from urllib.parse import quote
import time
import os
import japanize_kivy # 日本語表示
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.uix.widget import Widget

keyword = 'JAL ニュース'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"

class newsw(Widget):
    pass

class newsapp(App):
    def build(self):
        return get_news()


class get_news():
    def get_search_html(keyword, page):
        start = "&start=" + str(page * 10) # 次ページstart=10
        url = 'https://www.google.com/search?q=' + quote(keyword) + start 
        
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req) as res:
            body = res.read()
        return body
    
    def news():
        max_page = 1
        contents = []
        contents_u = []


        for page in range(max_page):
            html = get_search_html(keyword, page)
            soup = BeautifulSoup(html, 'html.parser')

            elemg = soup.select('div.yuRUbf > a ')
            elemori = soup.select('div.yuRUbf > a > h3')
            #URL
            print(elemg[1].attrs['href'])
            
            #title
            print(elemori[1])
            print(len(elemori))
            for i in range(len(elemori)):
                contents.append(elemori[i])
                contents_u.append(elemg[i].attrs['href'])

            print(contents)
            
            # title_text = soup.find('title').get_text()
            # print(title_text)

            time.sleep(3) # アクセス制限対策
            
        str1 ='''
        <html>
        <head>
        <meta charset="utf-8">
        <title>news</title>
        </head>
        <body>
        '''

        for j in range(len(contents)):
            str2 = "<p>" + str(contents[j]) + str("</p>")
            str3 = str("<a href='") + str(contents_u[j]) + str("'> URL </a>")
            str1 += str2
            str1 += str3

        with open( 'news.html', 'w', encoding='utf-8' ) as f1: 
            f1.write( str1 )  
        
    news() 

if __name__ == '__main__':
    newsapp().run()