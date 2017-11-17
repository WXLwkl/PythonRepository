#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/13.
#  Filename: use_asyncio

import asyncio

'''
asyncio的编程模型就是一个消息循环。
我们从asyncio模块中直接获取一个EventLoop的引用，
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
'''

# @asyncio.coroutine把一个generator标记为coroutine类型，
# 然后，我们就把这个coroutine扔到EventLoop中执行。
# @asyncio.coroutine
# def hello():
#     print('Hello, world!')
#     #异步调用 asyncio.sleep(1)
#     r = yield from asyncio.sleep(1)
#     print('Hello again')
#
# # 获取EventLoop
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# import threading
# @asyncio.coroutine
# def hello():
#     print("Hello world! (%s)" % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # lgnore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 可见3个连接由一个线程通过coroutine并发完成