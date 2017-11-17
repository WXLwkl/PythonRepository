#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/6.
#  Filename: use_collections

from collections import namedtuple


# namedtuple
'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，
并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
'''
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

# 可以验证创建的Point对象是tuple的一种子类：
print(isinstance(p, Point))
print(isinstance(p, tuple))


# deque
# deque除了实现list的append()和pop()外，
# 还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])  # key2不存在，返回默认值

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：

from collections import OrderedDict

d = dict([('a', 1),('b', 2),('c', 3)])
print(d)
od = OrderedDict([('a', 1),('b', 2),('c', 3)])
print(od)
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys())) # 按照插入的Key的顺序返回


# Counter  Counter是一个简单的计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# Counter实际上也是dict的一个子类，
# 上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
