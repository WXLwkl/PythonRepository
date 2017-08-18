#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Base
#  PythonRepository
#  Created by xingl on 2017/8/8.

import time
'''
想在终端中直接打开.py文件

1、在.py文件的第一行加上一个特殊的注释：#!/user/bin/env python3
2、找到.py文件所在的文件夹后，在终端中输入命令给 .py文件以执行权限：chmod a+x *.py
'''



print("--->我的名字：%s\n职业：%s\n年龄：%d" %("xingl",'iOS开发工程师', 26))
print("我的名字：{name}，职业：{job}，年龄：{age}" .format(name='xingl',job='iOS开发工程师',age='26'))



print('\"hello world\"')

age = 10
if age > 8:
    print("YES")
else:
    print("NO")

xx = 10
xx += 2
print(xx)

print('I\'m \"OK\"!')

print('I\'m learning\nPython')

print('''line1
line2
line3''')

print('\\\t\\')
print(r'\\\t\\')

print(not True)

aa = 'ABC'
bb = aa
a = 'XYZ'
print(bb)

'''

标准数据类型
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）

'''
print('---------------  Number（数字） -----------------------')
# Python3 支持 int、float、bool、complex（复数）。

# isinstance(object, classinfo)
#如果参数object是classinfo的实例，或者object是classinfo类的子类的一个实例， 返回True。
# 如果object不是一个给定类型的的对象， 则返回结果总是False。

a, b, c, d = 3, 4, 5, 6

e = a + b #加法
print(e)

e = e - a #减法
print(e)

e = a * c #乘法
print(e)

e = a / d #除法，得到一个浮点数
print(e)

e = a // d #除法，得到一个整数
print(e)

e = c % a #取余
print(e)

e = a ** c #乘方
print(e)

print('-------------------  String（字符串） --------------------------')
'''

python字符串格式化符号:
符号       描述
%c     格式化字符及其ASCII码
%s     格式化字符串
%d     格式化整数
%u     格式化无符号整型
%o     格式化无符号八进制数
%x     格式化无符号十六进制数
%X     格式化无符号十六进制数（大写）
%f     格式化浮点数字，可指定小数点后的精度
%e     用科学计数法格式化浮点数
%E     作用同%e，用科学计数法格式化浮点数
%g     %f和%e的简写
%G     %f 和 %E 的简写
%p     用十六进制数格式化变量的地址

'''


str = 'Runoob'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个从头到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串

print("------转 义---------")
print('Ru\noob')
print(r'Ru\noob') # \ 可以用来转义，使用r可以让反斜杠不发生转义。

print("------索引值-----------")
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6]) # 索引值以 0 为开始值，-1 为从末尾的开始位置。

# str.capitalize() 返回一个首字母大写的字符串
str = "this is python"
print("%s" %(str.capitalize()))

# center() 返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
str = "[www.runoob.com]"
print ("str.center(40, '') : ", str.center(40, ''))

'''
str.count(sub, start= 0,end=len(string))
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

该方法返回子字符串在字符串中出现的次数。

'''
str="www.runoob.com"
sub='o'
print ("str.count('o') : ", str.count(sub))

sub='run'
print ("str.count('run', 0, 10) : ", str.count(sub, 0, 10))


'''
encoding -- 要使用的编码，如"UTF-8"。
errors -- 设置不同错误的处理方案。
默认为 'strict',意为编码错误引起一个UnicodeError。
其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'
以及通过 codecs.register_error() 注册的任何值。
'''

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))

"""
startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
如果参数 beg 和 end 指定值，则在指定范围内检查。

"""
str = "this is string example....wow!!!"
print (str.startswith( 'this' ))
print (str.startswith( 'string', 8))
print (str.startswith( 'this', 2, 4 ))

"""
suffix -- 该参数可以是一个字符串或者是一个元素。
start -- 字符串中的开始位置。
end -- 字符中结束位置。
返回值
如果字符串含有指定的后缀返回True，否则返回False。
"""

Str='Runoob example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 20))
suffix='run'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))


"""
expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
tabsize -- 指定转换字符串中的 tab 符号('\t')转为空格的字符数。
返回值
该方法返回字符串中的 tab 符号('\t')转为空格后生成的新字符串。
"""
str = "this is\tstring example....wow!!!"

print ("原始字符串: " + str)
print ("替换 \\t 符号: " +  str.expandtabs())
print ("使用16个空格替换 \\t 符号: " +  str.expandtabs(16))


"""
str.find(str, beg=0, end=len(string))

str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。
返回值 如果包含子字符串返回开始的索引值，否则返回-1。
"""

str1 = "Runoob example....wow!!!"
str2 = "exam";

print (str1.find(str2))
print (str1.find(str2, 5))
print (str1.find(str2, 10))

'''
index() 和find（）类似    如果包含子字符串返回开始的索引值，否则抛出异常。
'''
print (str1.index(str2))
print (str1.index(str2, 5))
# print (str1.index(str2, 10))

'''
rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
str -- 查找的字符串
beg -- 开始查找的位置，默认为0
end -- 结束查找位置，默认为字符串的长度。
'''
str1 = "this is really a string example....wow!!!"
str2 = "is"

print (str1.rfind(str2))

print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))

print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))

'''
rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。
str.rindex(str, beg=0 end=len(string))
str -- 查找的字符串
beg -- 开始查找的位置，默认为0
end -- 结束查找位置，默认为字符串的长度。
'''
str1 = "this is really a string example....wow!!!"
str2 = "is"

print (str1.rindex(str2))
# print (str1.rindex(str2,10))


'''
isalnum() 方法检测字符串是否由字母和数字组成。
'''
str = "runoob2016"  # 字符串没有空格
print(str.isalnum())

str = "www.runoob.com"
print(str.isalnum())
'''
isalpha() 方法检测字符串是否只由字母组成。
'''
str = "runoob"
print (str.isalpha())

str = "Runoob example....wow!!!"
print (str.isalpha())
'''
isdigit() 方法检测字符串是否只由数字组成。
'''
str = "123456";
print (str.isdigit())

str = "Runoob example....wow!!!"
print (str.isdigit())
'''
isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
'''
str = "runoob2016"
print (str.isnumeric())

str = "23443434"
print (str.isnumeric())

'''
isspace() 方法检测字符串是否只由空格组成
'''
str = "       "
print (str.isspace())

str = "Runoob example....wow!!!"
print (str.isspace())
'''
istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
'''
str = "This Is String Example...Wow!!!"
print (str.istitle())

str = "This is string example....wow!!!"
print (str.istitle())

# title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写。
str = "this is string example from runoob....wow!!!"
print (str.title())

"""
isupper() 方法检测字符串中所有的字母是否都为大写。
"""
str = "THIS IS STRING EXAMPLE....WOW!!!"
print (str.isupper())

str = "THIS is string example....wow!!!"
print (str.isupper())


'''
islower() 方法检测字符串是否由小写字母组成。
'''
str = "RUNOOB example....wow!!!"
print (str.islower())

str = "runoob example....wow!!!"
print (str.islower())


'''
isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
'''
str = "runoob2016"
print (str.isdecimal())

str = "23443434"
print (str.isdecimal())


'''
join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
'''

s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
'''
len() 方法返回字符串长度。
'''
str = "Runoob example....wow!!!";
print("字符串长度: ", len(str))

'''
ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
        如果指定的长度小于原字符串的长度则返回原字符串。
'''
str = "Runoob example....wow!!!"
print (str.ljust(50, '*'))

'''
rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
'''
str = "this is string example....wow!!!"
print (str.rjust(50, '*'))

# lower() 方法转换字符串中所有大写字符为小写。
str = "Runoob EXAMPLE....WOW!!!"
print( str.lower() )

# upper() 方法将字符串中的小写字母转为大写字母。
str = "this is string example from runoob....wow!!!"
print ("str.upper() : ", str.upper())

'''
swapcase() 方法用于对字符串的大小写字母进行转换。
'''
str = "this is string example....wow!!!"
print (str.swapcase())

str = "This Is String Example....WOW!!!"
print (str.swapcase())

'''
lstrip() 方法用于截掉字符串左边的空格或指定字符。
chars --指定截取的字符。
 返回截掉字符串左边的空格或指定字符后生成的新字符串。
'''
str = "     this is string example....wow!!!     !";
print( str.lstrip() );
str = "88888888this is string example....wow!!!8888888";
print( str.lstrip('8') );
'''
rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
'''
str = "     this is string example....wow!!!     "
print (str.rstrip())
str = "*****this is string example....wow!!!*****"
print (str.rstrip('*'))

'''
strip() 方法用于移除字符串头尾指定的字符（默认为空格）
相当于 lstrip() 和 rstrip（）
'''
str = "*****this is string example....wow!!!*****"
print (str.strip( '*' ))


'''
maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
注：两个字符串的长度必须相同，为一一对应的关系。
str.maketrans(intab, outtab)
'''
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print(str.translate(trantab))

'''
max() 方法返回字符串中最大的字母。
'''
str = "runoob"
print("最大字符: " + max(str))

# min() 方法返回字符串中最小的字母。
print("最小字符: " + min(str));

'''
replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次
返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。
'''

str = "www.w3cschool.cc"
print ("菜鸟教程新地址：", str)
print ("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))

str = "this is string example....wow!!!"
print (str.replace("i", "AA", 2))

"""
split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
str.split(str="", num=string.count(str)).
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。
"""
str = "this is string example....wow!!!"
print (str.split( ))
print (str.split('i',1))
print (str.split('w'))

'''
splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
如果参数 keepends 为 False或者空格，不包含换行符，
如果为 True，则保留换行符。
'''
str = 'ab c\n\nde fg\rkl\r\n'
print("", str.splitlines())
print("", str.splitlines(False))
print("", str.splitlines(True))

'''
zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0

'''
str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(40))
print ("str.zfill : ",str.zfill(50))



print("-------------- List（列表）--------------------")
list1 = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print(list1)            # 输出完整列表
print(list1[0])         # 输出列表第一个元素
print(list1[1:3])       # 从第二个开始输出到第三个元素
print(list1[2:])        # 输出从第三个元素开始的所有元素
print(tinylist * 2)    # 输出两次列表
print(list1 + tinylist) # 连接列表
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数。

a = [1, 2, 3, 4, 5, 6]
a[0] = 9  #与Python字符串不一样的是，列表中的元素是可以改变的：
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []   # 删除
print(a)

'''
len() 方法返回列表元素个数。
'''
list1 = ['Google', 'Runoob', 'Taobao']
print(len(list1))
list2 = list(range(5)) # 创建一个 0-4 的列表
print(list2)
print(len(list2))

'''
max() 方法返回列表元素中的最大值。
min() 方法返回列表元素中的最小值。
'''
list1, list2 = ['Google', 'Taobao', 'Runoob'], [456, 700, 200]

print ("list1 最大元素值 : %s list2 最大元素值 : %s" %(max(list1),max(list2)))
print ("list1 最小元素值 : %s list2 最小元素值 : %s" %(min(list1),min(list2)))
'''
list() 方法用于将元组转换为列表。
'''
# aTuple = (123, 'Google', 'Runoob', 'Taobao')
# list1 = list(aTuple)
# print ("列表元素 : ", list1)
# str = "Hello World"
# list2 = list(str)
# print ("列表元素 : ", list2)
'''
append() 方法用于在列表末尾添加新的对象。
'''
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)
'''
count() 方法用于统计某个元素在列表中出现的次数。
'''
aList = [123, 'Google', 'Runoob', 'Taobao', 123];

print ("123 元素个数 : ", aList.count(123))
print ("Runoob 元素个数 : ", aList.count('Runoob'))

'''
extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
'''
# list1 = ['Google', 'Runoob', 'Taobao']
# list2 = list(range(5)) # 创建 0-4 的列表
# list1.extend(list2)  # 扩展列表
# print("扩展后的列表：", list1)

'''
index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
'''
list1 = ['Google', 'Runoob', 'Taobao']
print ('Runoob 索引值为', list1.index('Runoob'))

'''
insert() 函数用于将指定对象插入列表的指定位置。
list.insert(index, obj)
'''
list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
print ('列表插入元素后为 : ', list1)

'''
pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
list.pop(obj=list[-1])
'''
list1 = ['Google', 'Runoob', 'Taobao']
list1.pop()
print ("列表现在为 : ", list1)
list1.pop(1)
print ("列表现在为 : ", list1)

'''
remove() 函数用于移除列表中某个值的第一个匹配项。
list.remove(obj)
'''
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.remove('Taobao')
print ("列表现在为 : ", list1)
'''
reverse() 函数用于反向列表中元素。
list.reverse()
'''
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.reverse()
print ("列表反转后: ", list1)

'''
sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
'''
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.sort()
print ("列表排序后 : ", list1)

'''
clear() 函数用于清空列表，类似于 del a[:]。
'''
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.clear()
print ("列表清空后 : ", list1)

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
del list1[:]
print ("xxx : ", list1)

'''
copy() 函数用于复制列表，类似于 a[:]。
'''
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1[:]
#list2 = list1.copy()
print ("list2 列表: ", list2)




print("------------ Tuple（元组） -----------------------")
tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple1)             # 输出完整元组
print(tuple1[0])          # 输出元组的第一个元素
print(tuple1[1:3])        # 输出从第二个元素开始到第三个元素
print(tuple1[2:])         # 输出从第三个元素开始的所有元素
print(tinytuple * 2)     # 输出两次元组
print(tuple1 + tinytuple) # 连接元组

#tuple[0] = 11  # 修改元组元素的操作是非法的
#print(tuple[0])

# 创建空元组
tup1 = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号
tup2 = (50,)
print(tup1,tup2)

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3)

# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，
tup = ('Google', 'Runoob', 1997, 2000)
print (tup)
del tup
#print(tup) //删除后不能访问，否则会报错

'''
len(tuple)
计算元组元素个数。
'''
tuple1 = ('Google', 'Runoob', 'Taobao')
print(len(tuple1))

'''
max(tuple)
返回元组中元素最大值。
'''
tuple2 = ('5', '4', '8')
print(max(tuple2))
print(type(max(tuple2)))

'''
tuple(seq)
将列表转换为元组。
'''
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)



print("-------------  Set（集合） ----------------------")

student = ({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'})
print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

print("-------------  Dictionary（字典） -------------------------------")
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print(dict['one'])       # 输出键为 'one' 的值
print(dict[2])           # 输出键为 2 的值
print(tinydict)          # 输出完整的字典
print(tinydict.keys())   # 输出所有键
print(tinydict.values()) # 输出所有值

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("字典长度 : %d" %  len(dict))
del dict['Name'] # 删除键 'Name'
dict.clear()     # 删除字典内所有元素。
del dict         # 删除字典

'''
copy() 函数返回一个字典的浅复制。
'''
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict2 = dict1.copy()
print ("新复制的字典为 : ",dict2)

'''
 fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
'''

# seq = ('name', 'age', 'sex')
#
# dict = dict.fromkeys(seq)
# print ("新的字典为 : %s" %  str(dict))
#
# dict = dict.fromkeys(seq, 10)
# print ("新的字典为 : %s" %  str(dict))

'''
get() 函数返回指定键的值，如果值不在字典中返回默认值
'''
dict = {'Name': 'Runoob', 'Age': 27}

print ("Age 值为 : %s" %  dict.get('Age'))
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))

'''
in 操作符用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false
'''
dict = {'Name': 'Runoob', 'Age': 7}

# 检测键 Age 是否存在
if  'Age' in dict:
    print("键 Age 存在")
else :
	print("键 Age 不存在")

# 检测键 Sex 是否存在
if  'Sex' in dict:
    print("键 Sex 存在")
else :
    print("键 Sex 不存在")


'''
items() 方法以列表返回可遍历的(键, 值) 元组数组。
'''
dict = {'Name': 'Runoob', 'Age': 7}

print ("Value : %s" %  dict.items())

'''
setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
'''
dict = {'Name': 'Runoob', 'Age': 7}

print ("Age 键的值为 : %s" %  dict.setdefault('Age', None))
print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))
print ("新字典为：", dict)

'''
update() 函数把字典dict2的键/值对更新到dict里
'''
dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female' }

dict.update(dict2)
print ("更新字典 dict : ", dict)

'''
--------------  Python数据类型转换  -----------------------------

int(x [,base])           将x转换为一个整数
float(x)                 将x转换到一个浮点数
complex(real [,imag])    创建一个复数
str(x)                   将对象 x 转换为字符串
repr(x)                  将对象 x 转换为表达式字符串
eval(str)                用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)                 将序列 s 转换为一个元组
list(s)                  将序列 s 转换为一个列表
set(s)                   转换为可变集合
dict(d)                  创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)             转换为不可变集合
chr(x)                   将一个整数转换为一个字符
unichr(x)                将一个整数转换为Unicode字符
ord(x)                   将一个字符转换为它的整数值
hex(x)                   将一个整数转换为一个十六进制字符串
oct(x)                   将一个整数转换为一个八进制字符串

'''




# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
print(len('中文'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))


#------  格式化  ---------
print('Hello, %s' % 'xingl')

print('Hi, %s, you have $%d.' % ('xingl', 1000000))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print ("我的名字是 :",'xingl')
print("【我的名字：%s\n 职业：%s\n 年龄：%d】" %("xingl",'iOS开发工程师', 26))

w = 4
h = 5
print("width =", w, " height =", h, " area =", w*h)


str = "现在"
# print("{0}时间为：{1}", (time.ctime(time.time())))
print("{0}时间为：{1}" .format(str, (time.ctime(time.time()))))

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
 # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))
print('{name}职业:{job}'.format(name='xingl', job='iOS开发'))

print("----------------------------------------------------")

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} 和 {1:10d}'.format(name, number))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; '
          'Taobao: {0[Taobao]:d}'.format(table))

# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
