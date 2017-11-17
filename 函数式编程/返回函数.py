#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/10/31.
#  Filename: 返回函数

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
# 现在f是一个求和函数，所以输出要用f()
print(f())

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print("两个函数是否相等", f1 == f2)

'''
闭包
注意到返回的函数在其定义内部引用了局部变量args，
所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
所以，闭包用起来简单，实现起来可不容易。
另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
'''
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# print('f1 =',f1(),' f2 =', f2(), ' f3 =',f3())  # f1 = 9  f2 = 9  f3 = 9
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()

print('f1 =',f1(),' f2 =', f2(), ' f3 =',f3())



# 匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
'''
匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
'''


# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2017-10-31')
f = now
print(f())
print(now.__name__)
print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():'% func.__name__)
        return func(*args, **kw)
    return wrapper

'''
观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
我们要借助Python的@语法，把decorator置于函数的定义处
'''
@log
def nowDate():
    print('2017-10-31')
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
nowDate()

# 把 @log 放到 now() 函数的定义处，相当于执行了语句：now = log(now)
'''
由于log()是一个decorator，返回一个函数，
所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，
因此，wrapper()函数可以接受任意参数的调用。
在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
'''

# 这个3层嵌套的decorator用法如下
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def nowDate2():
    print('2017-10-31')
nowDate2()
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的： now = log('execute')(now)

print(nowDate2.__name__)
'''
因为返回的那个wrapper()函数名字就是'wrapper'，
所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，
Python内置的functools.wraps就是干这个事的，
所以，一个完整的decorator的写法如下：
'''
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 或者针对带参数的decorator：

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#    偏函数
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换

print("233")
print(int('12345'))
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print("8进制",int('12345', base=8))
print('16进制',int('12345', 16))

'''
假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
'''
def int2(x, base=2):
    return int(x, base)
print(int2('100'))
'''
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
可以直接使用下面的代码创建一个新的函数int2：
'''
int2 = functools.partial(int, base=2)
print(int2('101'))




