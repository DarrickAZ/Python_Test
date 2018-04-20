print('##########################################错误、调试和测试#################################################')
# 错误、调试和测试
# 在程序运行过程中，总会遇到各种各样的错误。
# 有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这
# 种错误我们通常称之为bug，bug是必须修复的。
# 有的错误是用户输入造成的，比如让用户输入email地址，结果得到一个空字符串，
# 这种错误可以通过检查用户输入来做相应的处理。
# 还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满
# 了，写不进去了，或者从网络抓取数据，网络突然断掉了。这类错误也称为异常，
# 在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出。
# Python内置了一套异常处理机制，来帮助我们进行错误处理。
# 此外，我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。
# Python的pdb可以让我们以单步方式执行代码。
# 最后，编写测试也很重要。有了良好的测试，就可以在程序修改后反复运行，确保
# 程序输出符合我们编写的测试。
print('------------------------------------错误处理----------------------------------')
# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，
# 就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非
# 常常见。比如打开文件的函数 open()  ，成功时返回文件描述符（就是一个整
# 数），出错时返回 -1  。
# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混
# 在一起，造成调用者必须用大量的代码来判断是否出错：
# def foo():
#     r=some_function()
#     if r==(-1):
#         return (-1)
#     #do something
#     return r
#
# def bar():
#     r=foo()
#     if r==(-1):
#         print('Error')
#     else:
#         pass
# 一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出
# 一个错误信息）。
# 所以高级语言通常都内置了一套 try...except...finally...  的错误处理机
# 制，Python也不例外

print('------------------------------------try----------------------------------')
# try
# 让我们用一个例子来看看 try  的机制：
try:
    print('try...')
    r = 10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')
# 当我们认为某些代码可能会出错时，就可以用 try  来运行这段代码，如果执行出
# 错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即 except  语句
# 块，执行完 except  后，如果有 finally  语句块，则执行 finally  语句块，至
# 此，执行完毕。
# 上面的代码在计算 10 / 0  时会产生一个除法运算错误：
# try...
# except: division by zero
# finally...
# END
# 从输出可以看到，当错误发生时，后续语句 print('result:', r)  不会被执
# 行， except  由于捕获到 ZeroDivisionError  ，因此被执行。最
# 后， finally  语句被执行。然后，程序继续按照流程往下走。
# 如果把除数 0  改成 2  ，则执行结果如下:
# try...
# except: division by zero
# finally...
# END

# 由于没有错误发生，所以 except  语句块不会被执行，但是 finally  如果有，则
# 一定会被执行（可以没有 finally  语句）。
# 廖雪峰 JavaScript Python Git 教程
# 1011 错误处理
# 你还可以猜测，错误应该有很多种类，如果发生了不同类型的错误，应该由不同
# 的 except  语句块处理。没错，可以有多个 except  来捕获不同类型的错误：

# try:
# print('try...')
# r = 10 / int('a')
# print('result:', r)
# except ValueError as e:
# print('ValueError:', e)
# except ZeroDivisionError as e:
# print('ZeroDivisionError:', e)
# finally:
# print('finally...')
# print('END')

# # 引入日历模块
# import calendar
#
# # 输入指定年月
# yy = int(input("输入年份: "))
# mm = int(input("输入月份: "))
#
# # 显示日历
# print(calendar.month(yy, mm))

# 你还可以猜测，错误应该有很多种类，如果发生了不同类型的错误，应该由不同
# 的 except  语句块处理。没错，可以有多个 except  来捕获不同类型的错误：
try:
    print('try...')
    r=10/int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError')
except ZeroDivisionError as e:
    print('ZeroDivisionError')
finally:
    print('finally...')
print('END')

# nt()  函数可能会抛出 ValueError  ，所以我们用一个 except  捕
# 获 ValueError  ，用另一个 except  捕获 ZeroDivisionError  。
# 此外，如果没有错误发生，可以在 except  语句块后面加一个 else  ，当没有错
# 误发生时，会自动执行 else  语句：
# result: 5.0
# no error!
# finally...
# END
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自 BaseException  ，所以在
# 使用 except  时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打
# 尽”。比如：
# try:
# foo()
# except ValueError as e:
# print('ValueError')
# except UnicodeError as e:
# print('UnicodeError')
# 第二个 except  永远也捕获不到 UnicodeError  ，因
# 为 UnicodeError  是 ValueError  的子类，如果有，也被第一个 except  给捕获
# 了。
# Python所有的错误都是从 BaseException  类派生的，常见的错误类型和继承关系
# 看这里：

# 使用 try...except  捕获错误还有一个巨大的好处，就是可以跨越多层调用，比
# 如函数 main()  调用 foo()  ， foo()  调用 bar()  ，结果 bar()  出错了，这
# 时，只要 main()  捕获到了，就可以处理：
print('------------------------------------foo----------------------------------')
# try
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:',e)
    finally:
         print('finally...')

# Error: division by zero
# finally...
main()

print('------------------------------------调用堆栈----------------------------------')
# 调用堆栈
# 错误处理
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错
# 误信息，然后程序退出。来看看 err.py  ：
# def foo(s):
#     return 10/int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main():
#     bar('0')

#   File "E:/MyProject/EBusiness/PythonWorkSpace/Test/test08.py", line 188, in <module>
#   File "E:/MyProject/EBusiness/PythonWorkSpace/Test/test08.py", line 186, in main
# try...
#     bar('0')
# except: division by zero
# finally...
#   File "E:/MyProject/EBusiness/PythonWorkSpace/Test/test08.py", line 183, in bar
# END
#     return foo(s)*2
# try...
# ValueError
#   File "E:/MyProject/EBusiness/PythonWorkSpace/Test/test08.py", line 180, in foo
# finally...
#     return 10/int(s)
# END
# ZeroDivisionError: division by zero
main()

print('------------------------------------记录错误----------------------------------')
# 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束
# 了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同
# 时，让程序继续执行下去。
# Python内置的 logging  模块可以非常容易地记录错误信息：
import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

# main()
print('END')
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
# $ python3 err_logging.py
# ERROR:root:division by zero
# Traceback (most recent call last):
# File "err_logging.py", line 13, in main
# bar('0')
# File "err_logging.py", line 9, in bar
# return foo(s) * 2
# File "err_logging.py", line 6, in foo
# return 10 / int(s)
# ZeroDivisionError: division by zero
# END
# 通过配置， logging  还可以把错误记录到日志文件里，方便事后排查

print('------------------------------------记录错误----------------------------------')
# 抛出错误
# 错误处理
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不
# 是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错
# 误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然
# 后，用 raise  语句抛出一个错误的实例：
class FooError(ValueError):
     pass

def foo(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value:%s.' % s)
    return 10/n

# Traceback (most recent call last):
#   File "E:/MyProject/EBusiness/PythonWorkSpace/Test/test08.py", line 259, in <module>
#     foo('0')
#   File "E:/MyProject/EBusiness/PythonWorkSpace/Test/test08.py", line 256, in foo
#     raise FooError('invalid value:%s.' % s)
# __main__.FooError: invalid value:0.
# foo('0')
# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的
# 错误类型（比如 ValueError  ， TypeError  ），尽量使用Python内置的错误类型。
# 最后，我们来看另一种错误处理的方式：
def foo(s):
    n=int(s)
    if n==0:
        raise ValueError('invalid value %s .' %s)
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise

# bar()
# 在 bar()  函数中，我们明明已经捕获了错误，但是，打印一
# 个 ValueError!  后，又把错误通过 raise  语句抛出去了，这不有病么？
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便
# 于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方
# 式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把
# 问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去
# 处理。
# raise  语句如果不带参数，就会把当前错误原样抛出。此外，
# 在 except  中 raise  一个Error，还可以把一种类型的错误转化成另一种类型：
# try:
# 10 / 0
# except ZeroDivisionError:
# raise ValueError('input error!')
# 只要是合理的转换逻辑就可以，但是，决不应该把一个 IOError  转换成毫不相干
# 的 ValueError  。
# Python内置的 try...except...finally  用来处理错误十分方便。出错时，会分
# 析错误信息并定位错误发生的代码位置才是最关键的。
# 程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清
# 楚可能会抛出哪些错误，以及错误产生的原因。

print('------------------------------------调试----------------------------------')
# 调试
# 程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需
# 要修正。有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出
# 错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程
# 序的手段来修复bug。
# 第一种方法简单直接粗暴有效，就是用 print()  把可能有问题的变量打印出来看看：
def foo(s):
    n=int(s)
    print('>>> n = %d' % n)
    return 10/n

def main():
    foo('0')
# Traceback (most recent call last):
#   File "E:/MyProject/EBusiness/PythonWorkSpace/Test/test08.py", line 318, in <module>
#     main()
#   File "E:/MyProject/EBusiness/PythonWorkSpace/Test/test08.py", line 316, in main
#     foo('0')
#   File "E:/MyProject/EBusiness/PythonWorkSpace/Test/test08.py", line 313, in foo
#     return 10/n
# ZeroDivisionError: division by zero
# main()

# 执行后在输出中查找打印的变量值：
# $ python3 err.py
# >>> n = 0
# Traceback (most recent call last):
# ...
# ZeroDivisionError: integer division or modulo by zero
# 用 print()  最大的坏处是将来还得删掉它，想想程序里到处都是 print()  ，运
# 行结果也会包含很多垃圾信息。所以，我们又有第二种方法。

print('------------------------------------断言----------------------------------')
# 断言
# 凡是用 print()  来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n=int(s)
    assert n != 0,'n is zero'
    return 10/n

def main():
    foo('0')

# main()
# assert  的意思是，表达式 n != 0  应该是 True  ，否则，根据程序运行的逻
# 辑，后面的代码肯定会出错。
# 如果断言失败， assert  语句本身就会抛出 AssertionError  ：
# $ python3 err.py
# Traceback (most recent call last):
# ...
# AssertionError: n is zero!
# 程序中如果到处充斥着 assert  ，和 print()  相比也好不到哪去。不过，启动
# Python解释器时可以用 -O  参数来关闭 assert  ：
# $ python3 -O err.py
# Traceback (most recent call last):
# ...
# ZeroDivisionError: division by zero
# 关闭后，你可以把所有的 assert  语句当成 pass  来看

print('------------------------------------logging----------------------------------')
# logging
# 把 print()  替换为 logging  是第3种方式，和 assert  比， logging  不会抛出
# 错误，而且可以输出到文件：

import logging
logging.basicConfig(level=logging.INFO)

s='0'
n=int(s)
logging.info('n = %d' % n)
# print(10/n)
# logging.info()  就可以输出一段文本。运行，发现除
# 了 ZeroDivisionError  ，没有任何信息。怎么回事？
# 别急，在 import logging  之后添加一行配置再试试：
# import logging
# logging.basicConfig(level=logging.INFO)
# 看到输出了：
# $ python3 err.py
# INFO:root:n = 0
# Traceback (most recent call last):
# File "err.py", line 8, in <module>
# print(10 / n)
# ZeroDivisionError: division by zero
# 这就是 logging  的好处，它允许你指定记录信息的级别，
# 有 debug  ， info  ， warning  ， error  等几个级别，当我们指
# 定 level=INFO  时， logging.debug  就不起作用了。同理，指
# 定 level=WARNING  后， debug  和 info  就不起作用了。这样一来，你可以放心
# 地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# logging  的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地
# 方，比如console和文件。

print('------------------------------------pdb----------------------------------')
# pdb
# 调试
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行
# 状态。我们先准备好程序：
s='0'
n=int(s)
# print(10/n)
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行
# 状态。我们先准备好程序：
# # err.py
# s = '0'
# n = int(s)
# print(10 / n)
# 然后启动：
# $ python3 -m pdb err.py
# > /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
# -> s = '0'
# 以参数 -m pdb  启动后，pdb定位到下一步要执行的代码 -&gt; s = '0'  。输入
# 命令 l  来查看代码：
# (Pdb) l
# 1 # err.py
# 2 -> s = '0'
# 3 n = int(s)
# 4 print(10 / n)
# 输入命令 n  可以单步执行代码：
# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
# -> n = int(s)
# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
# -> print(10 / n)
# 任何时候都可以输入命令 p 变量名  来查看变量：
# 廖雪峰 JavaScript Python Git 教程
# 1023 调试
# (Pdb) p s
# '0'
# (Pdb) p n
# 0
# 输入命令 q  结束调试，退出程序：
# (Pdb) q
# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一
# 千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。
# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要 import pdb  ，然后，在
# 可能出错的地方放一个 pdb.set_trace()  ，就可以设置一个断点：
# # err.py
# import pdb
# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n)
# 运行代码，程序会自动在 pdb.set_trace()  暂停并进入pdb调试环境，可以用命
# 令 p  查看变量，或者用命令 c  继续运行：
# 廖雪峰 JavaScript Python Git 教程
# 1024 调试
# $ python3 err.py
# > /Users/michael/Github/learn-python3/samples/debug/err.py(7)<module>()
# -> print(10 / n)
# (Pdb) p n
# 0
# (Pdb) c
# Traceback (most recent call last):
# File "err.py", line 7, in <module>
# print(10 / n)
# ZeroDivisionError: division by zero
# 这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。

print('------------------------------------单元测试----------------------------------')
# 单元测试
# 如果你听说过“测试驱动开发”（TDD：Test-Driven Development），单元测试就不
# 陌生。
# 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
# 比如对函数 abs()  ，我们可以编写出以下几个测试用例：
# 1. 输入正数，比如 1  、 1.2  、 0.99  ，期待返回值与输入相同；
# 2. 输入负数，比如 -1  、 -1.2  、 -0.99  ，期待返回值与输入相反；
# 3. 输入 0  ，期待返回 0  ；
# 4. 输入非数值类型，比如 None  、 []  、 {}  ，期待抛出 TypeError  。
# 把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。
# 如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通
# 过，要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够
# 通过。
# 单元测试通过后有什么意义呢？如果我们对 abs()  函数代码做了修改，只需要再
# 跑一遍单元测试，如果通过，说明我们的修改不会对 abs()  函数原有的行为造成
# 影响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么
# 修改测试。
# 这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设
# 计的测试用例。在将来修改的时候，可以极大程度地保证该模块行为仍然是正确
# 的。
# 我们来编写一个 Dict  类，这个类的行为和 dict  一致，但是可以通过属性来访
# 问，用起来就像下面这样：
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

d=Dict(a=1,b=2)
#1
print(d['a'])

# 为了编写单元测试，我们需要引入Python自带的 unittest  模块，编写 mydict_test.py  如下：



























































