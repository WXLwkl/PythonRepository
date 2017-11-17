#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/1.
#  Filename: OOP_Pro   面向对象高级编程

# --------------------------------> 使用__slots__ <------------------------
print("--------------------------------> 使用__slots__ <------------------------")

class Student(object):
    pass

def set_age(self,age):  # 定义一个函数作为实例方法
    self.age = age


s = Student()
s.name = 'xingl'  # 动态给实例绑定一个属性
print(s.name)



# from types import MethodType
# s.set_age = MethodType(set_age, s) #给实例绑定一个方法
# s.set_age(25) #调用实例方法
# print(s.age)
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
# s2.set_age(33)
# print(s2.age)

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = set_score

s.set_score(40)
s2.set_score(88)
print(s.score)
print(s2.score)

'''
但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，
定义一个特殊的__slots__变量，来限制该class实例能添加的属性.
'''
class Student2(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

a = Student2()
a.name = 'xx'
a.age = 23
try:
    a.score = 99
except AttributeError as  error:
    print('AttributeError:', error)

print(a.age)
print(a.name)
# print(a.score) #报错
'''
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''
class GraduateStudent(Student2):
    pass

g = GraduateStudent()
g.score = 99
print(g.score)


# --------------------------------> 使用@property <------------------------
print("---------------------------> 使用@property <------------------------")
class Student1(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student1()
s.set_score(80)
print(s.get_score())
# s.set_score(1002)
# print(s.get_score())

# 对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Stu(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise  ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

ss = Stu()
ss.score = 60  #OK,实际转化为ss.set_score(60)
print(ss.score)

'''
注意到这个神奇的@property，我们在对实例属性操作的时候，
就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
'''

# --------------------------------> 多重继承 <------------------------
print("---------------------------> 多重继承 <------------------------")


class Animal(object):
    pass
# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, RunnableMixIn):
    pass

d = Dog()
d.run()

# ---------------------> 定制类 <------------
print('---------------------> 定制类 <------------')
class StudentX(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

print(StudentX('xingl'))
# 用print，打印出来的实例还是不好看
'''
这是因为直接显示变量调用的不是__str__()，而是__repr__()，
两者的区别是__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，
也就是说，__repr__()是为调试服务的。

解决办法是再定义一个__repr__()。
但是通常__str__()和__repr__()代码都是一样的，
所以，有个偷懒的写法： __repr__ = __str__
'''

'''
__iter__

如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。

我们以斐波那契数列为例，写一个Fib类，可以作用于for循环
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)

# 像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib1(object):
    def __getitem__(self, n):
        a,b = 1,1
        for x in range(n):
            a,b = b, a+b
        return a
f = Fib1()
print(f[0])
print(f[4])
# list有个神奇的切片方法：
print(list(range(100))[5:10])

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
f = Fib()
print(f[:10])
print(f[:10:2])

# __getattr__()
# Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
class Student(object):
    def __init__(self):
        self.name = 'xingl'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda :28  #返回函数也是完全可以的：
        raise AttributeError('\'Student\'objcet has no attribute\'%s\'' % attr)
    # def __call__(self):
    #     print('My name is %s.' % self.name)

s = Student()
print(s.name)
print(s.score)
print(s.age())
# print(s.abc)

"""
__call__

一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
能不能直接在实例本身上调用呢？在Python中，答案是肯定的。

任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
"""
class StudentY(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

s = StudentY('xingl')
s()

'''
我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
比如函数和我们上面定义的带有__call__()的类实例：
'''
# print(callable(Student()))
print(callable(max))
print(callable([1, 2, 3]))

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

# 使用枚举类

from enum import Enum,unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
print(Month.Jan)
for name, member in Month.__members__.items():
    print(name,'=>',member,',',member.value)



# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 #Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fir = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
for name, member in Weekday.__members__.items():
    print(name, '=>', member)

# 使用元类
'''
class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

type()函数既可以返回一个对象的类型，又可以创建出新的类型，
比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
'''
def fn(self, name = 'world'): #先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello',(object,),dict(hello=fn)) #创建Hello class
h = Hello()
h.hello("xingl")
print(type(Hello)) #<class 'type'>
print(type(h))     #<class '__main__.Hello'>
'''
要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple(元组)的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''

# metaclass 元类
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
# metaclass是类的模版，所以必须从‘type’类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self,value:self.append(value) #lambda函数也叫匿名函数
        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list,metaclass=ListMetaclass):
    pass
'''
当我们传入关键字参数metaclass时，魔术就生效了，
它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：
    1、当前准备创建的类的对象；
    2、类的名字；
    3、类继承的父类集合；
    4、类的方法集合。
'''
L = MyList()
L.add(1)
print(L)

'''
ORM全称“Object Relational Mapping”，即对象-关系映射，
就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
这样，写代码更简单，不用直接操作SQL语句
'''
# 编写一个ORM框架
# 编写底层模块的第一步，就是先把调用接口写出来。
# 比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，
# 我们期待他写出这样的代码：
# class User(Model):
#     #定义类的属性到列的映射
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
# #创建一个实例
# u = User(id = 12345, name = 'xingl', email = 'qq@qq.com', password = 'my-pwd')
# #保存到数据库
# u.save()

# 实现该ORM

# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name,'varchar(100)')
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 下一步，就是编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" %(k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings #保存属性和列的映射关系
        attrs['__table__'] = name #假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
# 基类Model
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except keyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) value (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL:%s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    #定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
#创建一个实例
u = User(id = 12345, name = 'xingl', email = 'qq@qq.com', password = 'my-pwd')
#保存到数据库
u.save()






