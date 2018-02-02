#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2017/11/16.
__author__ = 'xingl'




age = 26

# print(u"age: {0:d} ".format(age))
print(f"age: {age} ")




import os
x = '/Users/xingl/Desktop/AppIcon/2@2x.png'
fileName = os.path.basename(x)
print(os.path.splitext(fileName)[0])


def hanshu(n):
    n_1 = 1
    n_2 = 1
    m = n
    sumn = 0
    for a in range(1, m+1):
        if m == 1:
            return n_1
        if m == 2:
            return n_2
        sumn = n_1 + n_2
        n_2 = n_1
        n_1 = sumn
        print(sumn, end=" ")

hanshu(20)

print('------')

# def hanshu2(n):
#     sumn = 0
#     m = n
#     for dix in range(1, 4):
#         m = m % 10
#         sumn = sumn + m ** 3
#         m = n // 10
#         if sumn == n:
#             print(n, end=" ")
#
# def hanshuL():
#     for b in range(1, 1000):
#         hanshu2(b)
# hanshuL()

# python-百钱买白鸡

'''
经典题目：有100文钱，要买100只鸡，公鸡5文一只，母鸡3文一只，小鸡三只一文，
问公鸡母鸡小鸡各多少只？
'''

for x in range(1, 20):
    for y in range(1, 33):
        z = 100 - y - x
        if z % 3 == 0 and 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：', x, '只', '母鸡：', y, '只', '小鸡：', z, '只')

