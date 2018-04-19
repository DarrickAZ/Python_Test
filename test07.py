print('##########################################面向对象高级编程#################################################')
# 面向对象高级编程
# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，
# 面向对象还有很多高级特性，允许我们写出非常强大的功能。
# 我们会讨论多重继承、定制类、元类等概念。
print('------------------------------------使用__slots__----------------------------------')
# 使用__slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该
# 实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    pass
#然后，尝试给实例绑定一个属性：
s=Student()
s.name='Michael'
#Michael
print(s.name)
#还可以尝试给实例绑定一个方法：
#定义一个函数作为实例方法
def set_age(self,age):
    self.age=age

from types import MethodType
#给实例绑定一个方法
s.set_age=MethodType(set_age,s)
#调用实例方法
s.set_age(25)
#25
print(s.age)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# >>> s2 = Student() # 创建新的实例
# >>> s2.set_age(25) # 尝试调用方法
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'set_age'
# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score=score

Student.set_score=MethodType(set_score,Student)
#给class绑定方法后，所有实例均可调用：
s.set_score(100)
#100
print(s.score)
s2=Student()
s2.set_score(99.99)
#99.99
print(s2.score)
# 通常情况下，上面的 set_score  方法可以直接定义在class中，但动态绑定允许我
# 们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
print('------------------------------------使用slots----------------------------------')
# 使用slots
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添
# 加 name  和 age  属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊
# 的 __slots__  变量，来限制该class实例能添加的属性：
class Student(object):
    #用tuple定义允许绑定的属性名称
    __slots__ = ('name','age')

s=Student()
s.name='Michael'
s.age=25
#25
print(s.age)
#AttributeError: 'Student' object has no attribute 'score'
#s.score=25

# 由于 'score'  没有被放到 __slots__  中，所以不能绑定 score  属性，试图绑
# 定 score  将得到 AttributeError  的错误。
# 使用 __slots__  要注意， __slots__  定义的属性仅对当前类实例起作用，对继
# 承的子类是不起作用的：
# >>> class GraduateStudent(Student):
# ... pass
# ...
# >>> g = GraduateStudent()
# >>> g.score = 9999
# 除非在子类中也定义 __slots__  ，这样，子类实例允许定义的属性就是自身
# 的 __slots__  加上父类的 __slots__  。
print('------------------------------------使用@property----------------------------------')
# 使用@property
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法
# 检查参数，导致可以把成绩随便改：
class Student(object):
    pass
s=Student()
s.score=99
# 这显然不合逻辑。为了限制score的范围，可以通过一个 set_score()  方法来设置
# 成绩，再通过一个 get_score()  来获取成绩，这样，在 set_score()  方法里，
# 就可以检查参数：
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s=Student()
s.set_score(60)
#60
print(s.get_score())
#s.set_score(9999)
#    raise ValueError('score must between 0 ~ 100!')ValueError: score must between 0 ~ 100!
#print(s.get_score())

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于
# 追求完美的Python程序员来说，这是必须要做到的！
# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一
# 样起作用。Python内置的 @property  装饰器就是负责把一个方法变成属性调用的：
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# >>> s = Student()
# >>> s.score = 60 # OK，实际转化为s.set_score(60)
# >>> s.score # OK，实际转化为s.get_score()
# 60
# >>> s.score = 9999
# Traceback (most recent call last):
# ...
# ValueError: score must between 0 ~ 100!
# 廖雪峰 JavaScript Python Git 教程
# 977 使用@property
# 注意到这个神奇的 @property  ，我们在对实例属性操作的时候，就知道该属性很
# 可能不是直接暴露的，而是通过getter和setter方法来实现的。
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
# class Student(object):
# @property
# def birth(self):
# return self._birth
# @birth.setter
# def birth(self, value):
# self._birth = value
# @property
# def age(self):
# return 2015 - self._birth
# 上面的 birth  是可读写属性，而 age  就是一个只读属性，因为 age  可以根
# 据 birth  和当前时间计算出来。
# @property  广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对
# 参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

print('------------------------------------多重继承----------------------------------')
# 多重继承
# 继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功
# 能。
# 回忆一下 Animal  类层次的设计，假设我们要实现以下4种动物：
# Dog - 狗狗；
# Bat - 蝙蝠；
# Parrot - 鹦鹉；
# Ostrich - 鸵鸟。
# 如果按照哺乳动物和鸟类归类，我们可以设计出这样的类的层次：

# 如果要再增加“宠物类”和“非宠物类”，这么搞下去，类的数量会呈指数增长，很明显
# 这样设计是不行的。
# 正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
#  多重继承
class Animal(object):
    pass
# 大类:
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
# 各种动物:
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
# 现在，我们要给动物再加上 Runnable  和 Flyable  的功能，只需要先定义
# 好 Runnable  和 Flyable  的类：
class Runnable(object):

    def run(self):
        print('Running...')

class Flyable(object):

    def fly(self):
        print('Flying...')

# 对于需要 Runnable  功能的动物，就多继承一个 Runnable  ，例如 Dog  ：
class Dog(Mammal,Runnable):
    pass
#对于需要 Flyable  功能的动物，就多继承一个 Flyable  ，例如 Bat  ：
class Bat(Mammal,Flyable):
    pass
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。

print('------------------------------------多重继承----------------------------------')
# MixIn
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如， Ostrich  继承
# 自 Bird  。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，
# 让 Ostrich  除了继承自 Bird  外，再同时继承 Runnable  。这种设计通常称之为
# MixIn。
# 为了更好地看出继承关系，我们把 Runnable  和 Flyable  改
# 为 RunnableMixIn  和 FlyableMixIn  。类似的，你还可以定义出肉食动
# 物 CarnivorousMixIn  和植食动物 HerbivoresMixIn  ，让某个动物同时拥有好
# 几个MixIn：
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass

# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通
# 过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# Python自带的很多库也使用了MixIn。举个例子，Python自带
# 了 TCPServer  和 UDPServer  这两类网络服务，而要同时服务多个用户就必须使
# 用多进程或多线程模型，这两种模型由 ForkingMixIn  和 ThreadingMixIn  提
# 供。通过组合，我们就可以创造出合适的服务来。
# 比如，编写一个多进程模式的TCP服务，定义如下

# class MyTCPServer(TCPServer, ForkingMixIn):
# pass
# 编写一个多线程模式的UDP服务，定义如下：
# class MyUDPServer(UDPServer, ThreadingMixIn):
# pass
# 如果你打算搞一个更先进的协程模型，可以编写一个 CoroutineMixIn  ：
# class MyTCPServer(TCPServer, CoroutineMixIn):
# pass
# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可
# 以快速构造出所需的子类。

print('------------------------------------定制类----------------------------------')
# 定制类
# 看到类似 __slots__  这种形如 __xxx__  的变量或者函数名就要注意，这些在
# Python中是有特殊用途的。
# __slots__  我们已经知道怎么用了， __len__()  方法我们也知道是为了能让
# class作用于 len()  函数。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

# str
# 我们先定义一个 Student  类，打印一个实例：
class Student(object):

     def __init__(self,name):
         self.name=name

#<__main__.Student object at 0x05311D50>
print(Student('Leo'))

# 打印出一堆 &lt;__main__.Student object at 0x109afb190&gt;  ，不好看。
# 怎么才能打印得好看呢？只需要定义好 __str__()  方法，返回一个好看的字符串
# 就可以了：
class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

#Student object (name:Leo)
print(Student('Leo'))
# 这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
# 但是细心的朋友会发现直接敲变量不用 print  ，打印出来的实例还是不好看：
# >>> s = Student('Michael')
# >>> s
# <__main__.Student object at 0x109afb310>
# 这是因为直接显示变量调用的不是 __str__()  ，而是 __repr__()  ，两者的区别
# 是 __str__()  返回用户看到的字符串，而 __repr__()  返回程序开发者看到的字
# 符串，也就是说， __repr__()  是为调试服务的。
# 解决办法是再定义一个 __repr__()  。但是通常 __str__()  和 __repr__()  代
# 码都是一样的，所以，有个偷懒的写法：
# class Student(object):
# def __init__(self, name):
# self.name = name
# def __str__(self):
# return 'Student object (name=%s)' % self.name
# __repr__ = __str__

print('------------------------------------iter----------------------------------')
# iter
# 如果一个类想被用于 for ... in  循环，类似list或tuple那样，就必须实现一
# 个 __iter__()  方法，该方法返回一个迭代对象，然后，Python的for循环就会不
# 断调用该迭代对象的 __next__()  方法拿到循环的下一个值，直到遇
# 到 StopIteration  错误时退出循环。
# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

class Fib(object):

    def __init__(self):
        #初始化两个计数器 a，b
        self.a,self.b=0,1

    def __iter__(self):
        #实例本身就是迭代对象，故返回自己
        return self

    def __next__(self):
        #计算下一个值
        self.a,self.b = self.b,self.a+self.b
        #退出循环条件
        if self.a >1000:
            raise StopIteration()
        #返回下一个值
        return self.a

for n in Fib():
    print(n)

print('------------------------------------getitem----------------------------------')
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是
# 不行，比如，取第5个元素：
#TypeError: 'Fib' object does not support indexing
# Fib()[5]
#要表现得像list那样按照下标取出元素，需要实现 __getitem__()  方法：
class Fib(object):

    def __getitem__(self, n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a

#现在就可以按下标进行访问了
#3
# print(Fib()[3])
# 但是list有个神奇的切片方法：
# >>> list(range(100))[5:10]
# [5, 6, 7, 8, 9]
# 对于Fib却报错。原因是 __getitem__()  传入的参数可能是一个int，也可能是一
# 个切片对象 slice  ，所以要做判断：
# 988 定制类
# class Fib(object):
# def __getitem__(self, n):
# if isinstance(n, int): # n是索引
# a, b = 1, 1
# for x in range(n):
# a, b = b, a + b
# return a
# if isinstance(n, slice): # n是切片
# start = n.start
# stop = n.stop
# if start is None:
# start = 0
# a, b = 1, 1
# L = []
# for x in range(stop):
# if x >= start:
# L.append(a)
# a, b = b, a + b
# return L
# 现在试试Fib的切片：
# >>> f = Fib()
# >>> f[0:5]
# [1, 1, 2, 3, 5]
# >>> f[:10]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 但是没有对step参数作处理：
# >>> f[:10:2]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 也没有对负数作处理，所以，要正确实现一个 __getitem__()  还是有很多工作要
# 做的。
# 廖雪峰 JavaScript Python Git 教程
# 989 定制类
# 此外，如果把对象看成 dict  ， __getitem__()  的参数也可能是一个可以作key
# 的object，例如 str  。
# 与之对应的是 __setitem__()  方法，把对象视作list或dict来对集合赋值。最后，
# 还有一个 __delitem__()  方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict
# 没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口

print('------------------------------------getattr----------------------------------')
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定
# 义 Student  类：
class Student(object):

    def __init__(self):
        self.name='Michael'

# 调用 name  属性，没问题，但是，调用不存在的 score  属性，就有问题了：
s=Student()
#Michael
print(s.name)
#AttributeError: 'Student' object has no attribute 'score'
# print(s.score)
# 错误信息很清楚地告诉我们，没有找到 score  这个attribute。
# 要避免这个错误，除了可以加上一个 score  属性外，Python还有另一个机制，那
# 就是写一个 __getattr__()  方法，动态返回一个属性。修改如下：
class Student(object):

    def __init__(self):
        self.name='Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

# 当调用不存在的属性时，比如 score  ，Python解释器会试图调
# 用 __getattr__(self, 'score')  来尝试获得属性，这样，我们就有机会返
# 回 score  的值：
s=Student()
#Michael
print(s.name)
#99
print(s.score)
# 返回函数也是完全可以的：
# class Student(object):
# def __getattr__(self, attr):
# if attr=='age':
# return lambda: 25
# 只是调用方式要变为：
# >>> s.age()
# 25
# 注意，只有在没有找到属性的情况下，才调用 __getattr__  ，已有的属性，比
# 如 name  ，不会在 __getattr__  中查找。

# 此外，注意到任意调用如 s.abc  都会返回 None  ，这是因为我们定义
# 的 __getattr__  默认返回就是 None  。要让class只响应特定的几个属性，我们
# 就要按照约定，抛出 AttributeError  的错误：








