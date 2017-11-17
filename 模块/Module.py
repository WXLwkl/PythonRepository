#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/10/31.
#  Filename: Module 模块
__author__ = 'xingl'

# 使用模块

import sys

def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__ == '__main__':
    test()
'''
当我们在命令行运行hello模块文件时，
Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
最常见的就是运行测试。
'''

'''
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等
'''
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

'''
我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，
这样，调用greeting()函数不用关心内部的private函数细节，
这也是一种非常有用的代码封装和抽象的方法，即：
   外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
'''


from PIL import Image
im = Image.open('cell的类型.png')
print(im.format, im.size, im.mode)




# if len(sys.argv) <= 1:
#     print ('\033[31m' + '请输入图片路径,eg: python autoExportAppIcon.py /path/xxx.png' + '\033[0m')
#     quit()
# ImageName = sys.argv[1]
# # print('图片名字为：' + ImageName)
# originImg = ''
# try:
#     originImg = Image.open(ImageName)
# except:
#     print ('\033[31m' + '\'' + ImageName + '\'' + '，该文件不是图片文件，请检查文件路径.' + '\033[0m')
#     quit()
# print(originImg.format, originImg.size, originImg.mode)


