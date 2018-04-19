print('##########################################面向对象编程#################################################')
###面向对象编程
# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思
# 想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执
# 行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切
# 割成小块函数来降低系统的复杂度。
# 而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收
# 其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各
# 个对象之间传递。
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对
# 象数据类型就是面向对象中的类（Class）的概念。
# 我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处。

# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
#而处理学生成绩可以通过函数实现，比如打印学生的成绩：
def print_score(std):
    print('%s: %s' %(std['name'],std['score']))
#Michael: 98
print_score(std1)

# 如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而
# 是 Student  这种数据类型应该被视为一个对象，这个对象拥
# 有 name  和 score  这两个属性（Property）。如果要打印一个学生的成绩，首先
# 必须创建出这个学生对应的对象，然后，给对象发一个 print_score  消息，让对
# 象自己把自己的数据打印出来

class Student(object):
    #初始化方法
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法
# （Method）。面向对象的程序写出来就像这样：
bart=Student('Darrick',59)
lisa=Student('Leo',69)
#Darrick: 59
bart.print_score()
#Leo: 69
lisa.print_score()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例
# （Instance）的概念是很自然的。Class是一种抽象概念，比如我们定义的Class
# ——Student，是指学生这个概念，而实例（Instance）则是一个个具体的
# Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。
# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据
# 的方法。

print('##########################################类和实例#################################################')
##类和实例
# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的
# 模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象
# 都拥有相同的方法，但各自的数据可能不同。
# 仍以Student类为例，在Python中，定义类是通过 class  关键字：
class Student(object):
    pass
# class  后面紧接着是类名，即 Student  ，类名通常是大写开头的单词，紧接着
# 是 (object)  ，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通
# 常，如果没有合适的继承类，就使用 object  类，这是所有类最终都会继承的类。
# 定义好了 Student  类，就可以根据 Student  类创建出 Student  的实例，创建实
# 例是通过类名+()实现的：
bart=Student()
#<__main__.Student object at 0x05471950>
print(bart)
#<class '__main__.Student'>
print(Student)

# 可以看到，变量 bart  指向的就是一个 Student  的实例，后面
# 的 0x10a67a590  是内存地址，每个object的地址都不一样，而 Student  本身则是
# 一个类。
# 可以自由地给一个实例变量绑定属性，比如，给实例 bart  绑定一个 name  属性：
bart.name='Leo.'
#Leo.
print(bart.name)

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须
# 绑定的属性强制填写进去。通过定义一个特殊的 __init__  方法，在创建实例的时
# 候，就把 name  ， score  等属性绑上去：
class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

# 注意到 __init__  方法的第一个参数永远是 self  ，表示创建的实例本身，因
# 此，在 __init__  方法内部，就可以把各种属性绑定到 self  ，因为 self  就指
# 向创建的实例本身。
# 有了 __init__  方法，在创建实例的时候，就不能传入空的参数了，必须传入
# 与 __init__  方法匹配的参数，但 self  不需要传，Python解释器自己会把实例
# 变量传进去：
bart = Student('Leo.',99)
#99
print(bart.score)
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例
# 变量 self  ，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没
# 有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
print('------------------------------------数据封装----------------------------------')
# 面向对象编程的一个重要特点就是数据封装。在上面的 Student  类中，每个实例
# 就拥有各自的 name  和 score  这些数据。我们可以通过函数来访问这些数据，比如打印一个学生的成绩：
def print_score(std):
    print('%s: %s' %(std.name,std.score))
#Leo.: 99
print_score(bart)

# 但是，既然 Student  实例本身就拥有这些数据，要访问这些数据，就没有必要从
# 外面的函数去访问，可以直接在 Student  类的内部定义访问数据的函数，这样，
# 就把“数据”给封装起来了。这些封装数据的函数是和 Student  类本身是关联起来
# 的，我们称之为类的方法：
class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s:%s' %(self.name,self.score))

# 要定义一个方法，除了第一个参数是 self  外，其他和普通函数一样。要调用一个
# 方法，只需要在实例变量上直接调用，除了 self  不用传递，其他参数正常传入：
bar = Student('Darrick',99)
#Darrick:99
bar.print_score()
# 这样一来，我们从外部看 Student  类，就只需要知道，创建实例需要给
# 出 name  和 score  ，而如何打印，都是在 Student  类的内部定义的，这些数据
# 和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
# 封装的另一个好处是可以给 Student  类增加新的方法，比如 get_grade  ：
class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s:%s' %(self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart=Student('Frank',99)
#A
print(bart.get_grade())

print('##########################################访问限制#################################################')
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法
# 来操作数据，这样，就隐藏了内部的复杂逻辑。
# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例
# 的 name  、 score  属性：
print('------------------------------------访问限制----------------------------------')
bart=Student('Darrick',88)
#88
print(bart.score)
bart.score=99
#99
print(bart.score)
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线 __  ，在
# Python中，实例的变量名如果以 __  开头，就变成了一个私有变量（private），只
# 有内部可以访问，外部不能访问，所以，我们把Student类改一改：
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self._score))

# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问 实例变
# 量.__name  和 实例变量.__score  了：
bart=Student('Darrick',99)
#AttributeError: 'Student' object has no attribute '__name'
#print(bart.__name)
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，
# 代码更加健壮。
# 但是如果外部代码要获取name和score怎么办？可以给Student类增
# 加 get_name  和 get_score  这样的方法：
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
         return self.__name

    def get_score(self):
        return self.__score

bart=Student('Frank',78)
#78
print(bart.get_score())
# 如果又要允许外部代码修改score怎么办？可以再给Student类增加 set_score  方法：
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
         return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score=score

bart=Student('Year','2015')
#2015
print(bart.get_score())
bart.set_score(2018)
#2018
print(bart.get_score())
# 你也许会问，原先那种直接通过 bart.score = 59  也可以修改啊，为什么要定义
# 一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
class Student(object):

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
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 需要注意的是，在Python中，变量名类似 __xxx__  的，也就是以双下划线开头，
# 并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变
# 量，所以，不能用 __name__  、 __score__  这样的变量名。
# 有些时候，你会看到以一个下划线开头的实例变量名，比如 _name  ，这样的实例
# 变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意
# 思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访
# 问 __name  是因为Python解释器对外把 __name  变量改成了 _Student__name  ，
# 所以，仍然可以通过 _Student__name  来访问 __name  变量：
# >>> bart._Student__name
# 'Bart Simpson'
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把 __name  改成
# 不同的变量名。
# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

print('##########################################继承和多态#################################################')
# 继承和多态
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base
# class、Super class）。
print('------------------------------------继承和多态----------------------------------')
# 比如，我们已经编写了一个名为 Animal  的class，有一个 run()  方法可以直接打印：
class Animal(object):
    def run(self):
        print('Animal is runing...')

# 当我们需要编写 Dog  和 Cat  类时，就可以直接从 Animal  类继承：
class Dog(Animal):
    pass
class Cat(Animal):
    pass

# 对于 Dog  来说， Animal  就是它的父类，对于 Animal  来说， Dog  就是它的子
# 类。 Cat  和 Dog  类似。
# 继承有什么好处？最大的好处是子类获得了父类的全部功能。由于 Animial  实现
# 了 run()  方法，因此， Dog  和 Cat  作为它的子类，什么事也没干，就自动拥有
# 了 run()  方法：
dog=Dog()
dog.run()
cat=Cat()
cat.run()
# Animal is runing...
# Animal is runing...
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')
dog=Dog()
dog.run()
cat=Cat()
cat.run()
# Dog is running...
# Cat is running...
# 当子类和父类都存在相同的 run()  方法时，我们说，子类的 run()  覆盖了父类
# 的 run()  ，在代码运行的时候，总是会调用子类的 run()  。这样，我们就获得
# 了继承的另一个好处：多态。
# 要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的
# 时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数
# 据类型，比如str、list、dict没什么两样
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
# 判断一个变量是否是某个类型可以用 isinstance()  判断：
#True
print(isinstance(a,list))
#True
print(isinstance(b,Animal))
#True
print(isinstance(c,Dog))
# 看来 a  、 b  、 c  确实对应着 list  、 Animal  、 Dog  这3种类型。
# 但是等等，试试：
#True
print(isinstance(c,Animal))
# 看来 c  不仅仅是 Dog  ， c  还是 Animal  ！
# 不过仔细想想，这是有道理的，因为 Dog  是从 Animal  继承下来的，当我们创建
# 了一个 Dog  的实例 c  时，我们认为 c  的数据类型是 Dog  没错，但 c  同时也
# 是 Animal  也没错， Dog  本来就是 Animal  的一种！
# 所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可
# 以被看做是父类。但是，反过来就不行：
#False
print(isinstance(b, Dog))
# Dog  可以看成 Animal  ，但 Animal  不可以看成 Dog  。
# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个 Animal  类型的变量：
def run_twice(animal):
     animal.run()
     animal.run()
# Animal is runing...
# Animal is runing...
print(run_twice(Animal()))
# 当我们传入 Cat  的实例时， run_twice()  就打印出：
print(run_twice(Cat()))
# Cat is running...
# Cat is running..
# 看上去没啥意思，但是仔细想想，现在，如果我们再定义一个 Tortoise  类型，也从 Animal  派生：
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
# 当我们调用 run_twice()  时，传入 Tortoise  的实例：
print(run_twice(Tortoise()))
# Tortoise is running slowly...
# Tortoise is running slowly...
# 你会发现，新增一个 Animal  的子类，不必对 run_twice()  做任何修改，实际
# 上，任何依赖 Animal  作为参数的函数或者方法都可以不加修改地正常运行，原因
# 就在于多态。
# 多态的好处就是，当我们需要传入 Dog  、 Cat  、 Tortoise  ……时，我们只需
# 要接收 Animal  类型就可以了，因为 Dog  、 Cat  、 Tortoise  ……都
# 是 Animal  类型，然后，按照 Animal  类型进行操作即可。由于 Animal  类型
# 有 run()  方法，因此，传入的任意类型，只要是 Animal  类或者子类，就会自动
# 调用实际类型的 run()  方法，这就是多态的意思：
# 对于一个变量，我们只需要知道它是 Animal  类型，无需确切地知道它的子类型，
# 就可以放心地调用 run()  方法，而具体调用的 run()  方法是作用
# 在 Animal  、 Dog  、 Cat  还是 Tortoise  对象上，由运行时该对象的确切类型
# 决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一
# 种 Animal  的子类时，只要确保 run()  方法编写正确，不用管原来的代码是如何
# 调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增 Animal  子类；
# 对修改封闭：不需要修改依赖 Animal  类型的 run_twice()  等函数。
# 继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而
# 任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。
# 比如如下的继承树：

print('------------------------------------静态语言 vs 动态语言----------------------------------')
## 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入 Animal  类型，则传入的对象必须
# 是 Animal  类型或者它的子类，否则，将无法调用 run()  方法。
# 对于Python这样的动态语言来说，则不一定需要传入 Animal  类型。我们只需要保
# 证传入的对象有一个 run()  方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')
# Start...
# Start...
print(run_twice(Timer()))
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来
# 像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一
# 个 read()  方法，返回其内容。但是，许多对象，只要有 read()  方法，都被视
# 为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真
# 正的文件对象，完全可以传入任何实现了 read()  方法的对象。
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增
# 自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的

print('##########################################获取对象信息#################################################')
###获取对象信息
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
print('------------------------------------使用type()----------------------------------')
# 首先，我们来判断对象类型，使用 type()  函数：
# 基本类型都可以用 type()  判断：
#<class 'int'>
print(type(123))
#<class 'str'>
print(type('str'))
#<class 'NoneType'>
print(type(None))
#如果一个变量指向函数或者类，也可以用 type()  判断：
#<class 'builtin_function_or_method'>
print(type(abs))
# 但是 type()  函数返回的是什么类型呢？它返回对应的Class类型。如果我们要
# 在 if  语句中判断，就需要比较两个变量的type类型是否相同：
#True
print(type(123)==type(456))
#True
print(type(123)==int)
#True
print(type('abc')==type('123'))
# True
print(type('abc')==str)
#False
print(type('abc')==type(123))

# 判断基本数据类型可以直接写 int  ， str  等，但如果要判断一个对象是否是函数
# 怎么办？可以使用 types  模块中定义的常量：
import types
def fn():
    pass
#True
print(type(fn)==types.FunctionType)
# >>> type(fn)==types.FunctionType
# True
# >>> type(abs)==types.BuiltinFunctionType
# True
# >>> type(lambda x: x)==types.LambdaType
# True
# >>> type((x for x in range(10)))==types.GeneratorType
# True
print('------------------------------------使用isinstance()----------------------------------')
# 使用isinstance()
# 对于class的继承关系来说，使用 type()  就很不方便。我们要判断class的类型，
# 可以使用 isinstance()  函数。
# 我们回顾上次的例子，如果继承关系是：
# object -> Animal -> Dog -> Husky
# 那么， isinstance()  就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
a=Animal()
d=Dog()
#True
print(isinstance(d,Animal))
# 能用 type()  判断的基本类型也可以用 isinstance()  判断：
# >>> isinstance('a', str)
# True
# >>> isinstance(123, int)
# True
# >>> isinstance(b'a', bytes)
# True
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是
# 否是list或者tuple：
# >>> isinstance([1, 2, 3], (list, tuple))
# True
# >>> isinstance((1, 2, 3), (list, tuple))
# True

print('------------------------------------使用dir()----------------------------------')
# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用 dir()  函数，它返回一个包含
# 字符串的list，比如，获得一个str对象的所有属性和方法：
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(dir('ABC'))
# 类似 __xxx__  的属性和方法在Python中都是有特殊用途的，比如 __len__  方法
# 返回长度。在Python中，如果你调用 len()  函数试图获取一个对象的长度，实际
# 上，在 len()  函数内部，它自动去调用该对象的 __len__()  方法，所以，下面
# 的代码是等价的：
#3
print(len('ABC'))
#3
print('ABC'.__len__())

#我们自己写的类，如果也想用 len(myObj)  的话，就自己写一个 __len__()  方法：
class MyDog(object):
    def __len__(self):
        return 100

dog=MyDog()
#100
print(len(dog))
# 剩下的都是普通属性或方法，比如 lower()  返回小写的字符串：
# >>> 'ABC'.lower()
# 'abc'

# 仅仅把属性和方法列出来是不够的，配合 getattr()  、 setattr()  以
# 及 hasattr()  ，我们可以直接操作一个对象的状态：
# >>> class MyObject(object):
# ... def __init__(self):
# ... self.x = 9
# ... def power(self):
# ... return self.x * self.x
# ...
# >>> obj = MyObject()
# 紧接着，可以测试该对象的属性：
# 廖雪峰 JavaScript Python Git 教程
# 966 获取对象信息
# >>> hasattr(obj, 'x') # 有属性'x'吗？
# True
# >>> obj.x
# 9
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# False
# >>> setattr(obj, 'y', 19) # 设置一个属性'y'
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# True
# >>> getattr(obj, 'y') # 获取属性'y'
# 19
# >>> obj.y # 获取属性'y'
# 19
# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# >>> getattr(obj, 'z') # 获取属性'z'
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'MyObject' object has no attribute 'z'
# 可以传入一个default参数，如果属性不存在，就返回默认值：
# >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 404
# 也可以获得对象的方法：
# 廖雪峰 JavaScript Python Git 教程
# 967 获取对象信息
# >>> hasattr(obj, 'power') # 有属性'power'吗？
# True
# >>> getattr(obj, 'power') # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
# >>> fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn() # 调用fn()与调用obj.power()是一样的
# 81
# 小结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的
# 数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如
# 果可以直接写：
# sum = obj.x + obj.y
# 就不要写：
# sum = getattr(obj, 'x') + getattr(obj, 'y')
# 一个正确的用法的例子如下：
# def readImage(fp):
# if hasattr(fp, 'read'):
# return readData(fp)
# return None
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方
# 法，如果存在，则该对象是一个流，如果不存在，则无法读取。 hasattr()  就派
# 上了用场。
# 廖雪峰 JavaScript Python Git 教程
# 968 获取对象信息
# 请注意，在Python这类动态语言中，根据鸭子类型，有 read()  方法，不代表该fp
# 对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只
# 要 read()  方法返回的是有效的图像数据，就不影响读取图像的功能。


print('##########################################获取对象信息#################################################')
# 实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过 self  变量：
print('------------------------------------获取对象信息----------------------------------')
# class Student(object):
# def __init__(self, name):
# self.name = name
# s = Student('Bob')
# s.score = 90
# 但是，如果 Student  类本身需要绑定一个属性呢？可以直接在class中定义属性，
# 这种属性是类属性，归 Student  类所有：
# class Student(object):
# name = 'Student'
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问
# 到。来测试一下：
# 廖雪峰 JavaScript Python Git 教程
# 970 实例属性和类属性
# >>> class Student(object):
# ... name = 'Student'
# ...
# >>> s = Student() # 创建实例s
# >>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
# >>> print(Student.name) # 打印类的name属性
# Student
# >>> s.name = 'Michael' # 给实例绑定name属性
# >>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
# >>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
# Student
# >>> del s.name # 如果删除实例的name属性
# >>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student
# 从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相
# 同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，
# 再使用相同的名称，访问到的将是类属性。









































