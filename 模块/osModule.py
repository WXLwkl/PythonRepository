#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 编程可执行文件 chmod a+x 文件名.py 这样直接拖到终端 回车

import os

rootPath = '/Users/xingl/Desktop'

# os.mkdir("%s/test" %rootPath) # 创建文件目录 (文件夹)
# os.makedirs("%s/test/a/b/c" %rootPath) # 创建多层次目录

# os.rmdir("%s/test" %rootPath) # 删除目录 (删除空目录)
# os.removedirs("%s/test/a/b/c" %rootPath) # 删除多级目录
# print(os.listdir('.')) # 列出当前文件夹里的文件以及目录 （不包含子目录）
# print(os.listdir('/')) # 跟目录
# print(os.getcwd()) #获取当前目录
# os.chdir() #切换目录


def dirList(path):
    fileList = os.listdir(path)
    # print(fPath)
    fList  = []
    for fileName in fileList:
        # fp = "%s/%s" %(fPath, fileName)
        # fList.append(fPath + '/' + fileName)
        fileP = os.path.join(path, fileName)
        if os.path.isdir(fileP):
            fList.append(dirList(fileP))
        # fList.append(fileP)
        else:
            fList.append(fileP)
    return fList

allfile = dirList('%s/testdir' %rootPath)
print(allfile)

print('============== 清屏 ===================')
g = os.walk(os.path.join(rootPath, "testdir"))
print(g)
for i in g:
    print(i)





def fun():
    global xxx  #把xxx生成全局变量
    # xxx = 50
    print(xxx)
fun()
print(xxx)