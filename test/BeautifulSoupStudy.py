#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/8/12.
__author__ = 'xingl'


from bs4 import BeautifulSoup
import requests

url = 'http://findingstar.com/'
r = requests.get(url)
# print(r.text)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup.title.string)
# print('--- head ---')
# print(soup.head)

# print(soup.div)

# divs = soup.div.children
# print(divs)
# print(type(divs))


print(soup.find_all(attrs="title"))


# for s in r.iter_lines():
    # soup = BeautifulSoup(s, 'lxml')
    # if soup.img:
    #     print('img标签的全部属性：', soup.img.attrs)
    #     print('img标签的src属性的值：', soup.img.attrs['src'])