###函数

##调用函数
#abs(有且仅有一个参数) 求绝对值
#100
print(abs(100))
#20
print(abs(-20))
#12.34
print(abs(12.34))
#有且只能接收一个参数 TypeError: abs() takes exactly one argument (2 given)
#print(abs(1,2))
#参数类型要求是整数
#TypeError: bad operand type for abs(): 'str'
#print(abs('a'))

#max函数，可接收任意多个参数
#2
print(max(1,2,-3))

#数据类型转换

#int 将其他数据类型转换为整数
#123
print(int('123'))
#12
print(int(12.34))
#float
#12.34
print(float('12.34'))
#str 将其他数据类型转换为字符串
#'1.23'
print(str(1.23))
print(str(100))
#bool
#True
print(bool(1))
#False
print(bool(''))
#True
print(bool(3>1))

#将一个函数名赋值给一个变量
a = abs;
#1
print(a(-1))

#hex()函数 转换为十六进制
#0x2d3
print(hex(723))


##定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
#调用自定义函数,如果没有return语句，函数执行完成后也会返回结果，只是结果为None
#20
print(my_abs(-20))
#定义一个什么事都不做的空函数，可以用pass语句
#pass可以作为占位符，没有的话文件会报错
def nop():
    pass

#参数检查
#TypeError: my_abs() takes 1 positional argument but 2 were given
#print(my_abs(1,2))
#TypeError: abs() takes exactly one argument (2 given)
#print(abs(1,2))

#修改自定义my_abs函数,当参数不为int和float的时候抛出异常
def my_abs_plus(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>0:
        return x
    else:
        return -x
#TypeError: bad operand type
#print(my_abs_plus('A'))
#2
print(my_abs_plus(2))

#返回多个值，例如坐标的计算,其实返回的还是一个tuple，python返回的是一个单一值
#导入math包，后续代码可以引用其中的sin,cos函数
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
#(45.98076211353316, 115.0)
print(move(20,100,30,math.pi/6))

#计算平方根math.sqrt()函数
import math
#3.0
print(math.sqrt(9))

##函数的参数
#位置参数,power(x)函数中 x 就是一个位置参数
def power(x):
    return x*x
#4
print(power(2))
#n次方的计算函数
def power3(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
#8
print(power3(2,3))

#默认参数
#n=2 就是一个默认参数
def powerN(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
#4 此时只传入了一个参数，但是有着默认值 所以也不会报错
print(powerN(2))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
# name: Darrick
# gender: F
# age: 6
# city: Beijing
print(enroll('Darrick','一年级'))
#只有与默认参数不一致的才会改变
# name: Leo
# gender: 二年级
# age: 6
# city: Tianjing
print(enroll('Leo','二年级',city='Tianjing'))

def add_end(L=[]):
    L.append('END')
    return L
#[1, 2, 'END']
print(add_end([1,2]))
#[3, 4, 'END']
print(add_end([3,4]))
#['END']
print(add_end())
#['END', 'END']
print(add_end())

#修改add_end()函数
def add_end_plus(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

#['END']
print(add_end_plus())
#['END']
print(add_end_plus())

#可变参数
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
#14
print(calc([1,2,3]))
#14
print(calc((1,2,3)))

#改为可变参数 numbers接收类型为tuple
def calcNum(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum
#14   可接收一个list
print(calcNum(1,2,3))
#0
print(calcNum())

num=[1,2,3]
#TypeError: can't multiply sequence by non-int of type 'list'
#print(calcNum(num))
#14  如果已经有了一个list
print(calcNum(*num))

#关键字参数
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
#name: Michael age: 30 other: {}
print(person('Michael',30))
#name: Bob age: 35 other: {'city': 'Beijing'}
print(person('Bob', 35, city='Beijing'))
#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
print(person('Adam', 45, gender='M', job='Engineer'))

#命名关键字参数
def person_plus(name,age,**kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
#name: Darrick age: 18 other: {'sex': '男', 'location': '湖北'}  此种方式还是没办法限制传入的命名参数
print(person_plus('Darrick',18,sex='男',location='湖北'))

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接
# 收 city  和 job  作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数 **kw  不同，命名关键字参数需要一个特殊分隔符 *  ， *  后面的
# 参数被视为命名关键字参数。
# 调用方式如下：
#Jack 24 Beijing Engineer
print(person('Jack', 24, city='Beijing', job='Engineer'))
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用
#TypeError: person() missing 1 required keyword-only argument: 'job'
#print(person('Jack',23,city='Tianjing'))

#参数组合
#其实就是 必选参数、默认参数、可变参数、关键字参数、和命名关键字参数
def f1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#a = 1 b = 2 c = 0 args = () kw = {}
print(f1(1,2))
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
#a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))

#a = 1 b = 2 c = 0 d = 99 kw = {}
print(f2(1,2,d=99))

##递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
#1
print(fact(1))
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120
#3   3*2*1
#RecursionError: maximum recursion depth exceeded in comparison
#栈溢出
#print(fact(1000))



































