#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/13.
#  Filename: 常见问题


# 如何获取当前路径
import os, sys
print(os.path.abspath('.'))

# 如何获取当前模块的文件名
print(__file__)
print(os.path.basename(__file__))

print(sys.argv)
print('--------')
print(sys.argv[0])
print('--------')
# argv的第一个元素永远是命令行执行的.py文件名。

# 如何获取当前Python命令的可执行文件路径
print(sys.executable)

