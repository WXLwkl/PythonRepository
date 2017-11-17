#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/1.
#  Filename: OOP


# ----------> 类和实例 <-----------
'''
面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
'''

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

print_score(std1)


'''
可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
'''
# 注意：特殊方法“init”前后有两个下划线！！！
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

'''
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了，
必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
'''

bart = Student('AA', 59)
bart.print_score()
print(bart.name)


# 数据封装  面向对象编程的一个重要特点就是数据封装。
'''
在上面的Student类中，每个实例就拥有各自的name和score这些数据。
我们可以通过函数来访问这些数据，比如打印一个学生的成绩
'''
def print_score(std):
    print('%s:%s' %(std.name,std.score))

print_score(bart)

# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：

class Student1(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

Tom = Student1('Tom',78)
a =  Tom.get_grade()
print(a)

# --------> 访问限制 <------------

bart = Student('Bart Simpson', 98)
print(bart.score)   #98
bart.score = 80
print(bart.score)   #80

'''
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
'''
class Student2(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

jary = Student2('Jary', 99)
print('get_name:',jary.get_name())
jary.set_score(88)
jary.print_score()
'''
这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

但是如果外部代码要获取name和score怎么办？
可以给Student类增加get_name和get_score这样的方法：
'''

# -------> 继承与多态 <----------
print('-------------------------> 继承与多态 <----------------------------')
'''
在OOP程序设计中，
当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）。
'''
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

d = Dog()
d.run()
'''
当子类和父类都存在相同的run()方法时，
我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
这样，我们就获得了继承的另一个好处：多态。
'''
# 判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(d, Dog))
print(isinstance(d, Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')



run_twice(Tortoise())

# ----------> 获取对象信息 <------------
print('--------------------> 获取对象信息 <----------------------')
# 基本类型都可以用type()判断：
print(type(123))
print(type('abc')==str)
# 判断基本数据类型可以直接写int，str等，
# 但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)
# 对于class的继承关系来说，使用type()就很不方便。
# 我们要判断class的类型，可以使用isinstance()函数。

class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
a = Animal()
d = Dog()
h = Husky()
print("isinstance判断",isinstance(h, Husky))
print("判断继承", isinstance(h, Dog))
print(isinstance(d, Husky))

# 能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance('a', str))
print(isinstance(123, int))
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

'''
使用dir()

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
比如，获得一个str对象的所有属性和方法：
'''
print(dir('ABC'))
'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，
实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
'''

print('ABC'.__len__(),'+',len('ABC'))


'''
仅仅把属性和方法列出来是不够的，
配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
'''
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return sef.x * self.x
obj = MyObject()

print(hasattr(obj,'x')) #有属性‘x’吗？
print(obj.x)

print('有属性‘y’吗',hasattr(obj, 'y')) #有属性‘y’吗？
setattr(obj,'y',19) #设置一个属性‘y’
print('有属性‘y’吗',hasattr(obj, 'y')) #有属性‘y’吗？
print('y =',getattr(obj, 'y')) #获取属性‘y’
print('y =',obj.y)

# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# getattr(obj, 'z') # 获取属性'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))

# 也可以获得对象的方法：
'''
hasattr(obj, 'power') # 有属性'power'吗？  True
getattr(obj, 'power') # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn() # 调用fn()与调用obj.power()是一样的  81
'''

# ------------------------> 实例属性和类属性 <-----------------------
print('------------------------> 实例属性和类属性 <-----------------------')

class Stu(object):
    def __init__(self, name):
        self.name = name

s = Stu('Bob')
s.score = 90
print(s.score)

class S(object):
    name = 'Student'
ss = S() # 创建实例ss
print(ss.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(ss.name) # 打印类的name属性

ss.name = 'xingl' # 给实例绑定name属性
print(ss.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(S.name) # 但是类属性并未消失，用Student.name仍然可以访问
del ss.name # 如果删除实例的name属性
print('删除后的名字',ss.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

'''
从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，
再使用相同的名称，访问到的将是类属性。
'''
