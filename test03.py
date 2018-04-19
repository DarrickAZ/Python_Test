###高级特性

##切片
# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前3个元素
#['Michael', 'Sarah', 'Tracy']
print(L[0:3])
#如果第一个索引是 0  ，还可以省略：
#['Michael', 'Sarah', 'Tracy']
print(L[:3])
#既然Python支持 L[-1]  取倒数第一个元素，那么它同样支持倒数切片
#['Bob', 'Jack']
print(L[-2:])
#['Bob']
print(L[-2:-1])

#构建0~99的数列
S=list(range(100))
#取出前10个数
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(S[:10])
#取出后10个数
#[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print(S[-10:])
#前11~20个数
#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(S[10:20])
#前10个数，每2个取一个
#[0, 2, 4, 6, 8]
print(S[:10:2])
#所有数，每5个取一个
#[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
print(S[::5])
#什么都不写，S[:],即可复制一个list
print(S[:])

#tuple也是一种list,唯一的区别是tuple是不可变的，因此tuple也可以进行切片操作，只是切片后的结果，仍然是tuple
tl=(1,2,3,4,5)
#(1, 2, 3)
print(tl[:3])
# 字符串 'xxx'  也可以看成是一种list，每个元素就是一个字符。因此，字符串也可
# 以用切片操作，只是操作结果仍是字符串：
#'ABC'
print('ABCDEFG'[:3])
#'ACEG'
print('ABCDEFG'[::2])

##迭代
# 如果给定一个list或tuple，我们可以通过 for  循环来遍历这个list或tuple，这种遍
# 历我们称为迭代（Iteration）
d={'a':1,'b':2,'c':3}
#循环遍历key值
for key in d:
    print(key)
#循环遍历vaule
for value in d.values():
    print(value)
#同时迭代key和value
for k,v in d.items():
    print(k,v)
#字符串也是可迭代对象
for ch in 'ABC中国人abc':
    print(ch)
#判断所要迭代对象，是否为一个真正的可迭代对象
from collections import Iterable
#True
print(isinstance('abc',Iterable))
#True
print(isinstance([1,2,3],Iterable))
#False
print(isinstance(123,Iterable))

#如果要对list进行像java一样的处理 ，可选Python内置的enumerate函数
# 0 A
# 1 B
# 2 C
for i,value in enumerate(['A','B','C']):
        print(i,value)
# 1 1
# 2 4
# 5 9
for x, y in [(1, 1), (2, 4), (5, 9)]:
     print(x, y)

##列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来
# 创建list的生成式。
#生成1~10的list序列
li=list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(li)
#如果要生成[1x1,2x2,3x3...10x10]怎么做？
L=[]
for x in range(1,11):
    L.append(x*x)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(L)
#简化上面循环
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x*x for x in range(1,11)])
#[4, 16, 36, 64, 100]  筛选出偶数
print([x * x for x in range(1, 11) if x % 2 == 0])
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']  两次循环生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

#三层和三层以上的循环就很少用到了。
# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和
# 目录名，可以通过一行代码实现：
import os
#列出目录下的所有文件
#['AndroidWorkSpace', 'apache-maven-3.3.3', 'beimi', 'CWorkSpace', 'eclipse', 'eclipse-jee-oxygen-R-win32-x86_64.zip',
# 'eclipse_EBusiness.lnk', 'GitRep', 'IDEAWorkSpace', 'JavaFXlogs', 'LazyLoad', 'Line01', 'Line02', 'NetBeansWorkSpace',
# 'NodeJSWorkSpace', 'PythonWorkSpace', 'rpc', 'rpc - 副本', 'ScanLogin', 'SpringBoot-Learning', 'SpringBoot-Learning -
# 副本 - 副本', 'springboot-learning-example - 副本', 'springcloud-learning-example - 副本', 'WeiXinApp', 'WorkSpace', 'WorkSpaceBlog',
# '深入理解Java虚拟机：JVM高级特性与最佳实践（第2版）源代码', '深入理解Java虚拟机：JVM高级特性与最佳实践（第2版）源代码.zip']
print([d for d in os.listdir('E:\\MyProject\\EBusiness')])

#for  循环其实可以同时使用两个甚至多个变量，比如 dict  的 items()  可以同时迭代key和value：
d={'x':'A','y':'B','z':'C'}
# x A
# y B
# z C
for k,v in d.items():
    print(k,v)
#列表生成式，也可以使用2个变量来生成list
#['x=A', 'y=B', 'z=C']
print([k+'=' +v for k,v in d.items()])
#将所有字符串变为小写
L = ['Hello', 'World', 'IBM', 'Apple']
#['hello', 'world', 'ibm', 'apple']
print([s.lower() for s in L])
nL= ['Hello', 'World', 18, 'Apple', None]
#['hello', 'world', 'apple']
print([s.lower() for s in nL if isinstance(s,str)])

##生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯
# 定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空
# 间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白
# 浪费了。
# Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式
# 的 []  改成 ()  ，就创建了一个generator：
L=[x*x for x in range(10)]
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(L)
g=(x*x for x in range(10))
#0
print(next(g))
#1
print(next(g))
for n in g:
    print(n)

# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都
# 可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
         #yield b 变成generator
         print(b)
         a, b = b, a + b
         n = n + 1
    return 'done'

#
print(fib(6))

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# 调用该generator时，首先要生成一个generator对象，然后用 next()  函数不断获
# 得下一个返回值：
#1
# print(next(odd()))
# print(next(odd()))
# print(next(odd()))

o=odd()
print(next(o))
print(next(o))
print(next(o))
#StopIteration
#print(next(o))

## 迭代器
# 我们已经知道，可以直接作用于 for  循环的数据类型有以下几种：
# 一类是集合数据类型，如 list  、 tuple  、 dict  、 set  、 str  等；
# 一类是 generator  ，包括生成器和带 yield  的generator function。
# 这些可以直接作用于 for  循环的对象统称为可迭代对象： Iterable  。
# 可以使用 isinstance()  判断一个对象是否是 Iterable  对象：
from collections import Iterable
#True
print(isinstance([],Iterable))
#True
print(isinstance((),Iterable))
#可以使用 isinstance()  判断一个对象是否是 Iterator  对象 next()函数
from collections import Iterator
#False
print(isinstance([],Iterator))
#True
print(isinstance((x for x in range(10)),Iterator))




###生成器Generator和yield的进一步说明
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式
# 的 []  改成 ()  ，就创建了一个generator：
# >>> L = [x * x for x in range(10)]
# >>> L
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> g = (x * x for x in range(10))
# >>> g
# <generator object <genexpr> at 0x1022ef630>
# 创建 L  和 g  的区别仅在于最外层的 []  和 ()  ， L  是一个list，而 g  是一个
# generator。
# 我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素
# 呢？
# 如果要一个一个打印出来，可以通过 next()  函数获得generator的下一个返回
print('#############################################################')
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #yield b
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#
print(fib(2))

def fibG(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
#
print(next(fibG(2)))
print(next(fibG(2)))
print(next(fibG(2)))
print(next(fibG(2)))
print(next(fibG(2)))
# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇
# 到 return  语句或者最后一行函数语句就返回。而变成generator的函数，在每次
# 调用 next()  的时候执行，遇到 yield  语句返回，再次执行时从上次返回
# 的 yield  语句处继续执行。

















