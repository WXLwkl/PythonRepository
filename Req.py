#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/6/15.
__author__ = 'xingl'


import urllib.request
import urllib.parse

url = 'http://www.baidu.com'
header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

request = urllib.request.Request(url, headers=header)
reponse = urllib.request.urlopen(request).read()

fhandle = open("./baidu.html", "wb")
fhandle.write(reponse)
fhandle.close()




