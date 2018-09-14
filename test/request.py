#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/6/20.
__author__ = 'xingl'

'''
urllib2是python自带的模块，不需要下载，urllib2在python3.x中被改为urllib.request。
'''

from urllib import request


url = "http://www.baidu.com"

print("第一种方法")
response1 = request.urlopen(url)
print("状态码：", response1.getcode())
#获取网页内容
html = response1.read()
#设置编码格式
# print(html.decode('utf8'))
#关闭
response1.close()

print("第二种方法")
request2 = request.Request(url)
request2.add_header('user-agent', 'Mozilla/5.0')
response2 = request.urlopen(request2)
print("状态码：", response2.getcode())
#获取网页内容
html2 = response2.read()
#设置编码格式
# print(html2.decode('utf8'))
#关闭
response2.close()

print("第三种方法  使用cookie")
import http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
request.install_opener(opener)
response3 = request.urlopen(url)
print(cookie)
html3 = response3.read()
# print(html3.decode('utf8'))
response3.close()