#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Test
#  PythonRepository
#  Created by xingl on 2017/7/28.

import time

ticks = time.time()
print("当前时间戳为：", ticks)
# 获取当前时间
# 从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
localTime = time.localtime(time.time())
print("本地时间为：", localTime)

# 获取格式化的时间
# 你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为：", localtime)

str = "现在"
# print("{0}时间为：{1}", (time.ctime(time.time())))
print("{0}时间为：{1}" .format(str, (time.ctime(time.time()))))


# 格式化日期
# 我们可以使用 time 模块的 strftime 方法来格式化日期，

# 格式化成2017-03-29 13:53:08形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Wed Mar 29 13:55:10 2017形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Wed Mar 29 13:55:10 2017"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


'''
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''



# 获取某月日历
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import calendar

cal = calendar.month(2017, 3)
print("以下输出2017年3月份的日历:")
print(cal)

# time.asctime([tupletime])
# 接受时间元组并返回一个可读的形式为
# "Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
t = time.localtime()
print("time.asctime(t): %s " % time.asctime(t))

# time.ctime([secs])
# 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
print ("time.ctime() : %s" % time.ctime())


# time.sleep(secs)
# 推迟调用线程的运行，secs指秒数。
print("Start : %s" % time.ctime())
time.sleep( 2 )
print("End   : %s" % time.ctime())


t = (2017, 3, 29, 17, 3, 38, 1, 48, 0)
secs = time.mktime( t )
print ("time.mktime(t) : %f" %  secs)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))

