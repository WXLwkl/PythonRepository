#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/4/28.
__author__ = 'xingl'




import requests
import json

req = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip=myip")

print(req.url)
print(req.json())
print(type(req.json()))

print(req.json()["data"]['ip'])