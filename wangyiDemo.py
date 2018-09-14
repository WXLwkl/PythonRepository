#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/9/13.
__author__ = 'xingl'

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.sina.com.cn/china/")
res.encoding = 'utf-8'
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
print(soup.select('div.feed-card-item'))

# for news in soup.select('div'):
    # print(news)

