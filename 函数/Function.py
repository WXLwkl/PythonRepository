#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/8/22.
#  Filename: Function 函数

import math

# 求绝对值的函数abs  abs()有且仅有1个参数
print(abs(10.34))
print(abs(-20))
# max()可以接收任意多个参数，并返回最大的那个,相反的，最小为 min()
x = max(2, 3, 1, -5)
print(x)

'''
函数名其实就是指向一个函数对象的引用，
完全可以把函数名赋给一个变量，
相当于给这个函数起了一个“别名”：
'''
a = abs
xx = a(-20)

#============  定义函数  ====

"""
在Python中，
定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。
"""
# 对参数类型做检查，只允许整数和浮点数类型的参数。
# 数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise  TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x

xx = my_abs(-20)
print(xx)

'''
空函数
如果想定义一个什么事也不做的空函数，可以用pass语句
缺少了pass，代码运行就会有语法错误。
'''
age = 26
if age >= 18:
    pass
else:
    print(age < 18)

# 返回多个值

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny
r = move(100,100,60,math.pi / 6)
print(r)

# 计算平方根可以调用math.sqrt()函数：
aa = math.sqrt(2)
print(aa)



#--------------------> 函数的参数 <-------------

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2,3))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 1))
print(power(5, 3))

#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3]))

print(calc((1, 3, 5, 7)))

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2, 3))
print(calc(1, 3, 5, 7))
# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
# 这种写法当然是可行的，问题是太繁琐，
# 所以Python允许你在list或tuple前面加一个*号，
# 把list或tuple的元素变成可变参数传进去
print(calc(*[1, 2, 3]))
print(calc(*(1, 3, 5, 7)))

#关键字参数
'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])
# 当然，上面复杂的调用可以用简化的写法：
'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
'''
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 命名关键字参数
'''
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
至于到底传入了哪些，就需要在函数内部通过kw检查。
'''
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下
def person(name, age, *, city, job):
    print(name, age, city, job)

'''
和关键字参数**kw不同，
命名关键字参数需要一个特殊分隔符*，
*后面的参数被视为命名关键字参数。
'''
person('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# person('Jack', 26, 'Beijing', 'Engineer')

# 命名关键字参数可以有缺省值，从而简化调用：

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('xingl', 26, job='Engineer')

'''
参数组合
在Python中定义函数，
可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)



#---------> 递归函数 <-------
'''
move(3, 'A', 'B', 'C')
A-->C
A-->B
C-->B
A-->C
B-->A
B-->C
A-->C
'''
def move(n, a, b, c):
    if n == 1:
        print(a + '-->' + c)
        return
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')
