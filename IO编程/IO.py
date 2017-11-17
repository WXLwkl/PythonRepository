#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/3.
#  Filename: IO

# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数
# 标示符'r'表示读，这样，我们就成功地打开了一个文件
f = open('/Users/xingl/Desktop/log.txt','r')
# 调用read()方法可以一次读取文件的全部内容
print(f.read())
# 最后一步是调用close()方法关闭文件
f.close()

try:
    r = open('/Users/xingl/Desktop/log.txt','r')
finally:
    if r:
        r.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# with open('/Users/xingl/Desktop/log.txt', 'r') as f:
#     print(f.read())

# 如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便：
with open('/Users/xingl/Desktop/log.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉

# 二进制文件

# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
x = open('/Users/xingl/Desktop/cell的类型.png', 'rb')
print(x.read())

# 字符编码

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
f = open('/Users/xingl/Desktop/log.txt', 'r', encoding='gbk')
print(f.read())
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
# 最简单的方式是直接忽略：
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')


# 写文件
# f = open('/Users/xingl/Desktop/log1.txt', 'w')
# f.write('百度一下，你就知道sss')
# f.close()

with open('/Users/xingl/Desktop/log1.txt', 'w') as f:
    f.write('Hello, world!')


# StringIO和BytesIO
# StringIO顾名思义就是在内存中读写str。

from io import StringIO, BytesIO
str = StringIO()
str.write('hello')
str.write(' ')
str.write('world!')
print(str.getvalue())  #getvalue()方法用于获得写入后的str。

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

ss = StringIO('Hello!\nHi!\nGoobye!')
while True:
    s = ss.readline()
    if s == "":
        break
    print(s.strip())

'''
BytesIO
StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
'''
b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# 操作文件和目录
import os
print(os.name) # 操作系统类型 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 要获取详细的系统信息，可以调用uname()函数
print(os.uname())  # uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 环境变量
print(os.environ)
print(os.environ.get('PATH'))


# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
'''
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
'''
print(os.path.join('/Users/xingl/Desktop/', 'testdir'))
# 然后创建一个目录:
# os.mkdir('/Users/xingl/Desktop/testdir')
# 删掉一个目录:
# os.rmdir('/Users/xingl/Desktop/testdir')

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('/Users/xingl/Desktop/testdir/file.txt'))

# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))

# 对文件重命名:
# os.rename('log1.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')

import shutil

shutil.copyfile('/Users/xingl/Desktop/log.txt','/Users/xingl/Desktop/12321/log.txt')

# 当前目录下的所有目录，只需要一行代码：
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 要列出所有的.py文件，也只需一行代码
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


# 序列化
import pickle
d = dict(name='Bob', age=20, score=98)
pickle.dumps(d)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object

# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。

# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# JSON

import json
print(json.dumps(d))  #dumps()方法返回一个str，内容就是标准的JSON。

json_str = '{"age":20, "score":88, "name":"xingl"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('xingl', 27, 99)
print(json.dumps(s,default=student2dict))
# print(json.dumps(s,default=lambda obj:obj.__dict__))
'''
如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))
'''
# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))