#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/1/3.
__author__ = 'xingl'

import urllib
from urllib import request

# 1、直接用urllib.request模块的urlopen（）获取页面，
# data的数据格式为bytes类型，需要decode（）解码，转换成str类型。
'''
urlopen返回对象提供方法:
read(), readline() ,readlines(), fileno(), close() ：对HTTPResponse类型数据进行操作
info()：返回HTTPMessage对象，表示远程服务器返回的头信息
getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
geturl()：返回请求的url
'''
# file = urllib.request.urlopen('http://www.baidu.com')
# print(file.geturl())
# print("---")
# print(file.info())
# print("---")
# print(file.getcode())
# print("----")
# data = file.read()
# data = data.decode('utf-8')
# print(data)


from urllib import request, parse
url = r'http://www.lagou.com/jobs/positionAjax.json?'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'Python'
}
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data)
page = request.urlopen(req).read()
page = page.decode('utf-8')