#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/8/17.
#  Filename: 2、条件判断

age = 20

if age >= 18:
    print("your age is", age)
    print('adult')
else:
    print("your age is too younger")


age1 = 3
if age1 >= 18:
    print('adult')
elif age1 >= 6:
    print('teenager')
else:
    print('kid')


age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# input()读取用户的输入  input()返回的数据类型是str
birth = int(input('birth:'))

if birth < 2000:
    print("00前")
else:
    print("00后")


# -------------- 循环 ---------------------

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
# range(5)生成的序列是从0开始小于5的整数
print(list(range(5)))

sum2 = 0
for x in range(101):
    sum2 = x + sum2
print(sum2)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

for i in range(1,11,2): # range(a, b) 生产数x  a <= x < b
    print(i)

sum3 = 0
for i in range(1, 100, 2):
    sum3 = sum3 + i
print(sum3)