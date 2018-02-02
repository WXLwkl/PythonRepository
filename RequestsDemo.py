#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/1/3.
__author__ = 'xingl'

import requests

# #get请求方法
# r = requests.get("http://itunes.apple.com/lookup?id=1121152696")
#
# print((type(r)))
# #打印get请求的状态码
# print(r.status_code)
# #查看请求的数据类型，可以看到是json格式，utf-8编码
# print(r.headers['content-type'])
# print(r.encoding)
# #打印请求到的内容
# # print(r.text)
# print(r.json())
# #输出json格式数据
# print("cookies: ", r.cookies)

params = {'id': 1121152696}
# headers = {'content-type': 'application/json'}
# r = requests.get("http://itunes.apple.com/lookup", params=params, headers=headers)
# print(r.url)
# print(r.json())


payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://itunes.apple.com/lookup", data=params)

print(r.text)