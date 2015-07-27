#!/usr/bin/python3
#coding: utf-8
'''
#而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。
#函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

#Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

#1---高阶函数
#-1-1-变量可以指向函数
#如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？用代码验证一下：
f = abs
print(f(-12))
#成功！说明变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。

#-1-2-函数名也是变量
#那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
#把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！

#当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复abs函数，请重启Python交互环境。

#注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。

#-1-3-传入函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

#一个最简单的高阶函数：
def add(x, y, f):
    return f(x) + f(y)
print(add(-3, 9, abs))
#编写高阶函数，就是让函数的参数能够接收别的函数
#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

#1---map/reduce
#Python内建了map()和reduce()函数。
#---map---
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

#举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6])
print(list(r))
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
#map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
print(list(map(str, [1, 2, 3, 4])))

#---reduce---
#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))

#整理成一个str2int的函数就是：
from functools import reduce
def str2int(s):
    def fn(x,  y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

#还可以用lambda函数进一步简化成：
from functools import reduce
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！
'''
'''
#1---filter
#Python内建的filter()函数用于过滤序列。

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6])))

#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
#结果: ['A', 'B', 'C']
#可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#用filter求素数
#可以先构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#注意这是一个生成器，并且是一个无限序列。

#然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0
#最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
#这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
## 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
'''
'''
#1---sorted
#比较的过程必须通过函数抽象出来。通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1，这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序。
#Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))
#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序

#再看一个字符串排序的例子：
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#我们给sorted传入key函数，即可实现忽略大小写的排序：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
'''
'''
#2---返回函数
#-1-函数作为返回值
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

#我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f())
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

#-2-闭包
#注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

#另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())
#一个函数可以返回一个计算结果，也可以返回一个函数。

#返回一个函数时牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''
'''
#3---匿名函数
#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

#在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#通过对比可以看出，匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f(9))
#同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y
#Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
'''
'''
#4---装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2015-3-11')
f = now
f()
#函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
print(f.__name__)
#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2015-3-11')
now()
#把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#这个3层嵌套的decorator用法如下：
@log('execute')
def now():
    print('2015-3-25')
now()
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：
#now = log('execute')(now)
#我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

#以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：

#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__))
        return func(*args, **kw)
    return wrapper
#或者针对带参数的decorator：
import functools

def lot(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。

#在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

#decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
'''
#5---偏函数
#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
#在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print(int('12345'))
#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print(int('12345', base=8))
print(int('12345', 16))

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base=2)
print(int2('100000'))
#所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

#注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
print(int2('1000000', base=10))
#最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
int2 = functools.partial(int, base=2)
#实际上固定了int()函数的关键字参数base，也就是：
#int2('10010')
#相当于
#kw = {'base': 2}
#int('10010', **kw)
#当传入max2=functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
#max2(5, 6, 7)
#相当于args = (10, 5, 6, 7)
#max(*args)
#结果为10
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
