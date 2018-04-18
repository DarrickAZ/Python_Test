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













































































