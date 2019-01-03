#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-01-02 17:35
# @Author  : opsonly
# @Site    :
# @File    : xiushibaike.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup

url='https://www.qiushibaike.com/text/'

req = requests.get(url)


soup = BeautifulSoup(req.content,'html.parser')


con = soup.find(id='content-left')

con_list = con.find_all('div', class_="article")  # 找到文章列表


print(con_list)


for i in con_list:
    author = i.find('h2').string  # 获取作者名字
    content = i.find('div', class_='content').find('span').get_text()  # 获取内容
    stats = i.find('div', class_='stats')
    vote = stats.find('span', class_='stats-vote').find('i', class_='number').string
    comment = stats.find('span', class_='stats-comments').find('i', class_='number').string

    print("作者:%s\n内容：%s点赞：%s 评论：%s\n\n" % (author,content,vote,comment))