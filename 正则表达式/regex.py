#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/6.
#  Filename: regex


import re

'''
re模块
有了准备知识，我们就可以在Python中使用正则表达式了。
Python提供re模块，包含所有正则表达式的功能。
由于Python的字符串本身也用\转义，所以要特别注意：
'''

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None


test = '010-12345'
if re.match(r'^\d{3}\-\d{3,8}$', test):
    print('ok')
else:
    print('failed')

# 切分字符串
print('a b   c'.split(' '))
# 无法识别连续的空格，用正则表达式试试：
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
'''
分组

除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。
用()表示的就是要提取的分组（Group）。比如：

^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
'''
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。



t = '16:08:45'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print(re.match(r'^(\d+?)(0*)$', '102300').groups())




