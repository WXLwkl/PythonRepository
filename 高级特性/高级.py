#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/9/1.
#  Filename: 高级


# ------>  切片   <--------
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略： L[:3]
print(L[0:3])  #['Michael', 'Sarah', 'Tracy']

# Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片

print(L[-2:]) #['Bob', 'Jack']
print(L[-2:-1]) #['Bob']


L1 = list(range(100))
print(L1[:10])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L1[-10:]) #[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# 前10个数，每两个取一个：
print(L1[:10:2])  #[0, 2, 4, 6, 8]

# 所有数，每5个取一个：
print(L[::5]) #[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# tuple也是一种list，唯一区别是tuple不可变。
# 因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])


# -------> 迭代 <--------
# 在Python中，迭代是通过 for ... in来完成的
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for ch in 'ABCDE':
    print("-->", ch)

# 那么，如何判断一个对象是可迭代对象呢？
# 方法是通过collections模块的Iterable类型判断

from collections import Iterable, Iterator

x = isinstance('abc', Iterable) # str是否可迭代
print(x)
x = isinstance([1,2,3], Iterable) # list是否可迭代
print(x)
x = isinstance(123, Iterable) # 整数是否可迭代
print(x)

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['a','b','c']):
    print('{0}-->{1}' .format(i,value))


for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# -------> 列表生成式 <-----------

print(list(range(1,11)))
'''
但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
'''
L = []
for x in range(1,11):
    L.append(x * x)
print(L)
# 循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
print("上面的可以写成这样",[x * x for x in range(1, 11)])
'''
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，
十分有用，多写几次，很快就可以熟悉这种语法。
'''

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 11) if x % 2 == 0])

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x':'A','y':'B','z':'z'}
for k,v in d.items():
    print(k,'=', v)

# 因此，列表生成式也可以使用两个变量来生成list：
print([k + '=' + v for k, v in d.items()])

# 最后把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


# ------> 生成器 <-----

L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
for n in g:
    print(n)

# 迭代器
'''
可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：
'''

from collections import Iterable
print(isinstance([], Iterable)) #True

print(isinstance({}, Iterable)) #True

print(isinstance('abc', Iterable)) #True

print(isinstance((x for x in range(10)), Iterable)) # True

print(isinstance(100, Iterable)) #False

'''
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象：
'''
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator)) #True

print(isinstance([], Iterator))    #False
print(isinstance({}, Iterator))    #False
print(isinstance('abc', Iterator)) #False

'''
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：
'''
print(isinstance(iter([]), Iterator)) #True
print(isinstance(iter('abc'), Iterator)) #True



