#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/2.
#  Filename: ErrorDebugTest


try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 可以有多个except来捕获不同类型的错误：
try:
    print('开始----')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally----')
print('结束-----')

'''
int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，
用另一个except捕获ZeroDivisionError。

此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
'''
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
'''
使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
这时，只要main()捕获到了，就可以处理：
'''
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        print(bar('3'))
    except Exception as e:
        print('Error:', e)
    finally:
        print('Finally....')
main()


# 断言（assert） 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
def foo1(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10/n

def main1():
    print(foo1('1'))
main1()


import logging, pdb

# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# logging.info('n = %d' % n)
# print(10 / n)

# Python的调试器pdb  python3 -m pdb 文件名.py

# ------------> 测试 <-----------------

class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value


d = Dict(a = 1, b = 2)
print(d['a'])
print(d.b)











