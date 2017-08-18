#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/8/15.
#  Filename: ListAndTuple

# --------  list   ----------
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)   #['Michael', 'Bob', 'Tracy']
# len()函数可以获得list元素的个数
print(len(classmates)) #3

# list索引从0开始
print(classmates[0]) #Michael
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1]) #Tracy

classmates.append("Adam")  #['Michael', 'Bob', 'Tracy', 'Adam']
print(classmates)
classmates.insert(1, 'Jack') #['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
print(classmates)
# 要删除list末尾的元素，用pop()方法
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop()  #['Michael', 'Jack', 'Bob', 'Tracy']
print(classmates)
classmates.pop(1) #['Michael', 'Bob', 'Tracy']
print(classmates)
# 某个元素替换成别的元素
classmates[1] = 'Sarah'  #'Michael', 'Sarah', 'Tracy']
print(classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s)) #4


# --------------- tuple ----------
# tuple一旦初始化就不能修改
classmates1 = ('Michael', 'Bob', 'Tracy')
# classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，
# 你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
t1 = (1, 2)  #(1, 2)
t2 = ()   #()
t3 = (1,) #(1,)
# 注：定义只有一个元素的时候不能用 (1)表示，()可以表示tuple也可以表示数学公式中的小括号。
t4 = ('a', 'b', ['A', 'B'])
t4[2][0] = 'X'
t4[2][1] = 'Y'
print(t4) #('a', 'b', ['X', 'Y'])
