###函数式编程
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返
# 回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是
# 纯函数式编程语言。

##高阶函数
# 变量可以指向函数
# 以Python内置的求绝对值的函数 abs()  为例，调用该函数用以下代码：
#10
print(abs(-10))
#变量可以指向函数
#<built-in function abs>
#print(abs)
x=abs(-10)
#10
print(x)
#将函数赋值给变量
f=abs
#10
print(f(-10))

##传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个
# 函数作为参数，这种函数就称之为高阶函数
#一个最简单的高阶函数
def add(x,y,f):
    return f(x)+f(y)
#10
print(add(-1,9,abs))
#x = -1
#y = 9
#f = abs
#f(x) + f(y) ==> abs(-1) + abs(9) ==> 10
#return 10

#map/reduce Python内建了 map()  和 reduce()  函数。
#map()  函数接收两个参数，一个是函数，一个
# 是 Iterable  ， map  将传入的函数依次作用到序列的每个元素，并把结果作为新
# 的 Iterator  返回。
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6])
# map()  传入的第一个参数是 f  ，即函数对象本身。由于结果 r  是一
# 个 Iterator  ， Iterator  是惰性序列，因此通过 list()  函数让它把整个序列
# 都计算出来并返回一个list。
#[1, 4, 9, 16, 25, 36]
print(list(r))
#['1', '2', '3', '4']
print(list(map(str,[1,2,3,4])))

# reduce  把一个函数作用在一个序列 [x1, x2, x3,
# ...]  上，这个函数必须接收两个参数， reduce  把结果继续和序列的下一个元素
# 做累积计算，其效果就是：
#序列求和
from functools import reduce
def add(x,y):
    return x+y
#16
print(reduce(add,[1,3,5,7]))

def fn(x, y):
     return x * 10 + y
#13579
print(reduce(fn, [1, 3, 5, 7, 9]))
# 1 3
#1*10 + 3
#13*10 + 5
# 135*10 +7
# 1357*10 +9
#13579

#将str转为int的函数
# def char2num(s):
#     return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# #
# print(reduce(fn,map(char2num ,'13579')))

##filer
# Python内建的 filter()  函数用于过滤序列。
# 和 map()  类似， filter()  也接收一个函数和一个序列。和 map()  不同的
# 时， filter()  把传入的函数依次作用于每个元素，然后根据返回值是 True  还
# 是 False  决定保留还是丢弃该元素。
# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1
#[1, 5, 9, 15]
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()
#['A', 'B', 'C']
print(list(filter(not_empty,['A','','B',None,'C',' '])))

#定义一个生成器，生成无限序列
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#定义一个筛选函数
def _not_divisible(n):
    return lambda x:x%n>0

#定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 10:
        print(n)
    else:
        break

print('##################################Sorted 排序算法##################################')
###sorted 排序算法
# 排序算法
# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心
# 是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两
# 个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数
# 抽象出来。
# Python内置的 sorted()  函数就可以对list进行排序：
#[-21, -12, 5, 9, 36]
print(sorted([36, 5, -12, 9, -21]))
#按绝对值大小进行排序
#[5, 9, -12, -21, 36]
print(sorted(([36, 5, -12, 9, -21]),key=abs))
#字符串排序的例子
#['Credit', 'Zoo', 'about', 'bob']
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于 'Z' &lt; 'a'  ，
# 结果，大写字母 Z  会排在小写字母 a  的前面
#忽略大小写进行排序
#['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
#反向忽略大小写进行排序
#['Zoo', 'Credit', 'bob', 'about']
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))


###################################################返回函数#############################################################
###返回函数
# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
#定义一个一般求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
#但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以
# 不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
#调用lazy_sum()
#<function lazy_sum.<locals>.sum at 0x04E0C6A8>
print(lazy_sum(1,2,3))
#6 调用
# 当我们调用 lazy_sum()  时，返回的并不是求和结果，而是求和函数：
# >>> f = lazy_sum(1, 3, 5, 7, 9)
# >>> f
# <function lazy_sum.<locals>.sum at 0x101c6ed90>
# 调用函数 f  时，才真正计算求和的结果：
# 廖雪峰 JavaScript Python Git 教程
# 922 返回函数
# >>> f()
# 25
print(lazy_sum(1,2,3)())
# 请再注意一点，当我们调用 lazy_sum()  时，每次调用都会返回一个新的函数，
# 即使传入相同的参数：
# >>> f1 = lazy_sum(1, 3, 5, 7, 9)
# >>> f2 = lazy_sum(1, 3, 5, 7, 9)
# >>> f1==f2
# False
#f1()  和 f2()  的调用结果互不影响。

###闭包
# 注意到返回的函数在其定义内部引用了局部变量 args  ，所以，当一个函数返回了
# 一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起
# 来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了 f()  才
# 执行。我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

# 全部都是 9  ！原因就在于返回的函数引用了变量 i  ，但它并非立刻执行。等到3
# 个函数都返回时，它们所引用的变量 i  已经变成了 3  ，因此最终结果为 9  。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变
# 化的变量。


###################################################匿名函数#############################################################
# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
# 在Python中，对匿名函数提供了有限支持。还是以 map()  函数为例，计算
# f(x)=x<sup>2</sup>时，除了定义一个 f(x)  的函数外，还可以直接传入匿名函数：
#[1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#通过对比可以看出，匿名函数 lambda x: x * x  实际上就是：
def f(x):
    return x * x
# 关键字 lambda  表示匿名函数，冒号前面的 x  表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写 return  ，返回值就是该表达式的结果。

f = lambda x: x * x
#25
print(f(5))

print('############################################装饰器#################################################')
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
     print('2015-3-25')
f = now
#2015-3-25
print(f())
#now
print(now.__name__)
#now
print(f.__name__)

# 现在，假设我们要增强 now()  函数的功能，比如，在函数调用前后自动打印日
# 志，但又不希望修改 now()  函数的定义，这种在代码运行期间动态增加功能的方
# 式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日
# 志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def nowLog():
    print('2015-3-25')
# call nowLog():
# 2015-3-25
print(nowLog())

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。比如，要自定义log的文本：
def logH(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return  wrapper
    return decorator

@logH('execute')
def nowH():
    print('2015-3-23')
#execute nowH():
# 2015-3-23
print(nowH())
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：
#>>> now = log('execute')(now)

#不需要编写 wrapper.__name__ = func.__name__  这样的代码，Python内置
# 的 functools.wraps  就是干这个事的，所以，一个完整的decorator的写法如下：
import functools


print('############################################偏函数#################################################')
##偏函数
# Python的
# functools
# 模块提供了很多有用的功能，其中一个就是偏函数（Partial
# function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的
# 难度。而偏函数也可以做到这一点。举例如下：
# int()
# 函数可以把字符串转换为整数，当仅传入字符串时， int()
# 函数默认按
# 十进制转换：
print(int('12345'))
# 但 int()  函数还提供额外的 base  参数，默认值为 10  。如果传入 base  参数，就可以做N进制的转换：
#5349
print(int('12345', base=8))
#74565
print(int('12345',base=16))

# 假设要转换大量的二进制字符串，每次都传入 int(x, base=2)  非常麻烦，于
# 是，我们想到，可以定义一个 int2()  的函数，默认把 base=2  传进去：
def int2(x, base=2):
    return int(x, base)
# 这样，我们转换二进制就非常方便了：
#64
print(int2('1000000'))
#85
int2('1010101')
###偏函数
# functools.partial  就是帮助我们创建一个偏函数的，不需要我们自己定
# 义 int2()  ，可以直接使用下面的代码创建一个新的函数 int2  ：
import functools
int2 = functools.partial(int, base=2)
#64
print(int2('1000000'))
#85
print(int2('1010101'))

# 所以，简单总结 functools.partial  的作用就是，把一个函数的某些参数给固定
# 住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# 注意到上面的新的 int2  函数，仅

max2 = functools.partial(max, 10)
#10
print(max2(5,5,10))




