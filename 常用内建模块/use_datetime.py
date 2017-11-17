#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/6.
#  Filename: use_datetime

from datetime import datetime, timedelta, timezone
now = datetime.now()  #其类型是datetime
print(now)
dt = datetime(2017, 11, 6, 17, 5)
print(dt)
print(dt.timestamp()) #把datetime转换为timestamp
print(now.timestamp())

# timestamp转换为datetime   使用datetime提供的fromtimestamp()方法
t = 1509959100.0
print(datetime.fromtimestamp(t))    # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

# str转换为datetime 转换方法是通过datetime.strptime()实现
cday = datetime.strptime('2017-11-6 17:10:50', '%Y-%m-%d %H:%M:%S')
print(cday)


# datetime转换为str
print(now.strftime('%a,%b %d %H:%M'))

# datetime加减  需要导入timedelta
print(now + timedelta(hours=1))  # + 就是向未来的时间计算
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
dtn = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dtn)

# 时区转换  通过utcnow()拿到当前的UTC时间
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print("北京时间：%s" % bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo: %s' % tokyo_dt)

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo2: %s' % tokyo_dt2)



