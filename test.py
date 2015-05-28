#!/usr/bin/python
#coding: utf-8

'''-1---Some Coding Style---
#!/usr/bin/env python
More precisely, the first or second line must match the regular
    expression "coding[:=]\s*([-\w.]+)"
#coding: utf-8
#coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding=<encoding name> :
'''

'''-2-
print "Hello Python!\n"

#',' will print as a space like ' '
print 'hello', 'Pyhton', '!\n'

#the func of input string as default
name = raw_input()
print name

#the func of input value as default 
i = input()
if i>0:
    print 1
else:
    print 0

a = 1

if a :
    print 1
else:
    print 0

#使用r"" 或 r''表示里面的字符串不使用转义
#print r'\\', "\\"
#'''
#如果换行比较多,'''...'''可以表示多行内容
#print '''line1
#line2
#line3'''

#print r'''line\\
#         line2'''
'''-3-
#逻辑运算:and or not
#空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
print 3>2

#Python是动态语言,可以把任意类型的数据赋值给变量,同一变量可以反复赋值,
#而且可以是不同类型的变量
a = 123
print a
a = 'wang'
print a

#在Python中，通常用全部大写的变量名表示常量. Python是大小写敏感的语言
PI = 3.1415926
print PI

#ord()和chr()函数，可以把字母和对应的数字相互转换
print chr(65)
print ord('a')

print '中文'

#len()函数可以返回字符串的长度
print len('wang')

#把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')

#把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法
print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#格式化输出: %s %f %d %x
print 'Hello, %s' % 'world'
print  'Hi, %s, you have $%d.' % ('Michael', 1000000)
print '%2d-%02d' % (3, 1)
print  '%.2f' % 3.1415926
print  'Age: %s. Gender: %s' % (25, True)
print u'Hi, %s' % u'Michael'
print  'growth rate: %d %%' % 7
#Python 2.x版本虽然支持Unicode，但在语法上需要'xxx'和u'xxx'两种字符串表示方式。
#在Python 3.x版本中，把'xxx'和u'xxx'统一成Unicode编码，即写不写前缀u都是一样的，而以字节形式表示的字符串则必须加上b前缀：b'xxx'。

#---list---
#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print classmates, len(classmates)
print classmates[0], classmates[1], classmates[2]

#区最后一个元素时,可以用-1做索引,以此类推，可以获取倒数第2个、倒数第3个：
print  classmates[-1], classmates[-2]

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
#也可以把元素插入到指定的位置，比如索引号为1的位置
#要删除list末尾的元素，用pop()方法
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates
classmates.pop()
print classmates
classmates.pop(1)
print classmates
classmates[1] = 'Sarah'
print classmates

#list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print L

#list元素也可以是另一个list
#要拿到'php'可以写s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到
s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)

#如果一个list中一个元素也没有，就是一个空的list，它的长度为0
L = []
print L, len(L)

'''
'''-5-
#---tuple--
#另一种有序列表叫元组：tuple, tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
#其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print t

#如果要定义一个空的tuple，可以写成()
t = ()
print t

#但是，要定义一个只有1个元素的tuple，如果你这么定义：
t = (1)
#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print t

#“可变的”tuple：
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t
#tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，
#指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

'''

#---条件判断和循环---
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
else:
    print 'your age is', age
    print 'teenager'
#elif是else if的缩写，完全可以有多个elif  
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
    print 'wang'
else:
    print 'kid'


