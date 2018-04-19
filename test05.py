###模块
print('############################################模块#################################################')
# 在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。为了编写可维护的代码，我们把很多
# 函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在Python中，一个.py文
# 件就称之为一个模块（Module）。使用模块有什么好处？最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块
# 编写完毕，就可以被其他地方引用。我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。使用模块还可以
# 避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲
# 突。但是也要注意，尽量不要与内置函数名字冲突。点这里查看Python的所有内置函数。你也许还想到，如果不同的人编写的模块名相同怎么办？
# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。举个例子，一个 abc.py  的文件就是一个名字叫 abc
# 的模块，一个 xyz.py  的文件就是一个名字叫 xyz  的模块。现在，假设我们的 abc  和 xyz  这两个模块名字与其他模块冲突了，于是我们可以
# 通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如 mycompany  ，按照如下目录存放：

print('##########################################使用模块#################################################')
# 第1行和第2行是标准注释，第1行注释可以让这个 hello.py  文件直接在
# Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'Michael Liao'
import sys
def test():
    args=sys.argv
    if len(args)==1:
            print('Hello,World!!!')
    elif len(args)==2:
            print('Hello, %S!' %args[1])
    else:
            print('Too many arguments!')
if __name__=='__main__':
    test()
# $ python3 hello.py
# Hello, world!
# $ python hello.py Michael
# Hello, Michael!
#导入模块
import hello
#Hello,World!
hello.test()

##作用域
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在
# Python中，是通过 _  前缀来实现的。
# 正常的函数和变量名是公开的（public），可以被直接引用，比如： abc  ， x123  ， PI  等；
# 类似 __xxx__  这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如
# 上面的 __author__  ， __name__  就是特殊变量， hello  模块定义的文档注释
# 也可以用特殊变量 __doc__  访问，我们自己的变量一般不要用这种变量名；
# 类似 _xxx  和 __xxx  这样的函数或变量就是非公开的（private），不应该被直接
# 引用，比如 _abc  ， __abc  等；
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
# 是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程
# 习惯上不应该引用private函数或变量。

def _private_1(name):
    return 'Hello,%s' % name

def _private_2(name):
    return 'Hi,%s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
#Hi,2
print(greeting('2'))

print('##########################################安装第三方模块#################################################')
# 安装第三方模块
# 在Python中，安装第三方模块，是通过包管理工具pip完成的。
# 如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。
# 如果你正在使用Windows，请参考安装Python一节的内容，确保安装时勾选
# 了 pip  和 Add python.exe to Path  。
# 在命令提示符窗口下尝试运行 pip  ，如果Windows提示未找到命令，可以重新运
# 行安装程序添加 pip  。
# 注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令
# 是 pip3  。
# 现在，让我们来安装一个第三方库——Python Imaging Library，这是Python下非常
# 强大的处理图像的工具库。不过，PIL目前只支持到Python 2.7，并且有年头没有更
# 新了，因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3。
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第
# 三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称
# 叫Pillow，因此，安装Pillow的命令就是：

from PIL import Image
im = Image.open('colorbar.png')
print(im.format, im.size, im.mode)
im.thumbnail((20, 10))
im.save('colorbarTemp.png', 'PNG')

# 模块搜索路径
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果
# 找不到，就会报错：
# >>> import mymodule
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ImportError: No module named mymodule

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模
# 块，搜索路径存放在 sys  模块的 path  变量中：
import sys
#['E:\\MyProject\\EBusiness\\PythonWorkSpace\\Test', 'E:\\MyProject\\EBusiness\\PythonWorkSpace\\Test', 'D:\\SoftWare\\Python36-32\\python36.zip', 'D:\\SoftWare\\Python36-32\\DLLs', 'D:\\SoftWare\\Python36-32\\lib', 'D:\\SoftWare\\Python36-32', 'D:\\SoftWare\\Python36-32\\lib\\site-packages', 'D:\\SoftWare\\PyCharm 2017.3.2\\helpers\\pycharm_matplotlib_backend']
print(sys.path)

# 如果我们要添加自己的搜索目录，有两种方法：
# 一是直接修改 sys.path  ，添加要搜索的目录：
# >>> import sys
# >>> sys.path.append('/Users/michael/my_py_scripts')
# 这种方法是在运行时修改，运行结束后失效。


# 第二种方法是设置环境变量 PYTHONPATH  ，该环境变量的内容会被自动添加到模
# 块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索
# 路径，Python自己本身的搜索路径不受影响















































