#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/7.
#  Filename: use_hashlib

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5x = hashlib.md5()
md5x.update('how to use md5 in '.encode('utf-8'))
md5x.update('python hashlib?'.encode('utf-8'))
print(md5x.hexdigest())




