#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/10/30.
#  Filename: 函数




# -----> 高阶函数 <-------

# map/reduce
# 以Python内置的求绝对值的函数abs()为例

x = abs(-10)
print(x)
'''
既然变量可以指向函数，函数的参数能接收变量，
那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
'''
def add(x, y, f):
    return f(x) + f(y)

def mm(n):
    return n * n

print(add(-5,6,mm))


def f(x):
    return x * x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))


L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

'''
reduce的用法。
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
from functools import reduce

def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))
# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

def fn(x, y):
    return x * 10 + y
print(reduce(fn,[1, 3, 5, 7, 9]))
'''
如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，
我们就可以写出把str转换为int的函数
'''

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print('字符串的',reduce(fn,map(char2num, '13579')))



# 练习

def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def fm(x, y):
    return x * y

def prod(L):
    return reduce(fm,L);

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# filter    Python内建的filter()函数用于过滤序列
'''
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A','B',None,'C',' '])))
'''
注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
'''

def is_palindrome(n):
    return str(n) == str(n)[::-1]
print('aa', list(filter(is_palindrome,range(1,1000))))

# sorted  排序算法
# Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，
# 例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))


# 一个字符串排序的例子：
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


print(sorted([1,54,23,56,33],reverse=True))



