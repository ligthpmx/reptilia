#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-01-31 09:05
# @Author  : opsonly
# @Site    : 
# @File    : jianshuHot.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup
baseUrl = 'https://www.jianshu.com'
url = 'https://www.jianshu.com/trending/monthly?utm_medium=index-banner-s'
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

obj = requests.get(url=url,headers=headers)

req = BeautifulSoup(obj.content,'html.parser')


con_list = req.find_all('a', class_="title")  # 找到文章列表

for i in con_list:

    articleUrl = baseUrl + i['href']
    print('Title:',i.string)
    print('Url:',articleUrl)
    print('***********')
