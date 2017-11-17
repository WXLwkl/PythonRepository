#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/8/18.
#  Filename: 3、DictAndSet


# ---------------  dictionary

d = {'Michael': 95, 'Bob': 80, 'Tracy': 88}
print(d["Bob"])  # 80
# 增加
d['Jack'] = 99  #{'Michael': 95, 'Bob': 80, 'Tracy': 88, 'Jack': 99}
print(d)
# 删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')  # {'Michael': 95, 'Tracy': 88, 'Jack': 99}
print(d)
# 修改
d["Tracy"] = 85  # {'Michael': 95, 'Tracy': 85, 'Jack': 99}
print(d)



#判断字典中是否存在 某key
print("Tracy" in d)  # True
# 尝试根据key获取对应的value，如果key不存在，则返回默认值
x = d.get('Bobx', -1)  # -1
print(x)

#------------- set ---
'''
set和dict类似，也是一组key的集合，但不存储value。
由于key不能重复，所以，在set中，没有重复的key。
'''
s = set([1, 2, 3]) # {1, 2, 3}
print(s)
# 增加
s.add(4) #{1, 2, 3, 4}
# 删除
s.remove(2) # {1, 3, 4}
print(s)


s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
ss1 = s1&s2 # {2, 3}
ss2 = s1|s2 # {1, 2, 3, 4}
print(ss1)
print(ss2)

