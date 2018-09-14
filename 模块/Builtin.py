#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/4/20.
__author__ = 'xingl'


#        内置函数
print(abs(-10))  #  abs 绝对值

print(max([1,2,3,56,78,87,32,43,24])) # max min 最大值 最小值

s = "hello"
len(s)                # len 长度
l = [1,2,3,46,78,67,87,4,23]
print(len(l))

a = divmod(5, 2)
print(a)

print(pow(2,3))
print(pow(2,3,4))

print(round(12))  #获取浮点型数据

def f():
    pass

print(callable(f))  # callable 检测函数是否能调用


import re

r1 = r"\d{3,4}-?\d{8}"
a =  re.findall(r1, "010-123456789")
print(a)

p_tel = re.compile(r1)

x = p_tel.findall('010-123456789')
print(x)