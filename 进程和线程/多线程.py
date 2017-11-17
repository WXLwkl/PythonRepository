#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/3.
#  Filename: 多线程

import time,threading
'''
Python的标准库提供了两个模块：_thread和threading，
_thread是低级模块，threading是高级模块，对_thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
'''
# 新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)



# 假定这是你的银行存款:
balance = 0

lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
# def run_thread(n):
#     for i in range(1000000):
#         change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# ThreadLocal
# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。


# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    time.sleep(2)
    print('Hello, %s(in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name= 'Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name= 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
'''
join()的 总结:
    1 join方法的作用是阻塞主进程无法执行join以后的语句,专注执行多线程,必须等待多线程执行完毕之后才能执行主线程的语句。
    2 多线程多join的情况下,依次执行各线程的join方法,前一个结束之后,才能执行后一个。
    3 无参数,则等待到该线程结束,才开始执行下一个线程的join。
    4 设置参数后,则等待该线程N秒之后不管该线程是否结束，就开始执行后面的主进程。
'''

print('end。。。。')
