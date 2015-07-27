#!/usr/bin/python3
#coding: utf-8

'''-1---Some Coding Style---
#!/usr/bin/env python
#!/usr/bin/python3
#!/usr/bin/python
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

#the func of input string as default, raw_input()读取的内容永远以字符串的形式返回，
#把字符串和整数比较就不会得到期待的结果，必须先用int()把字符串转换为我们想要的整型：
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

#if判断条件还可以简写，比如写：
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = True
if x:
    print True

#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
names = ['wang', "yan"]
for name in names:
    print name
#如果要计算1-100的整数之和,ange()函数，可以生成一个整数序列，比如range(5)生成的序列是从0开始小于5的整数
sum = 0
for x in range(101):
    sum += x
print sum

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 99
while n>0:
    sum += n 
    n -= 2
print sum

#使用dict和set
#---dict---
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢
d = {'Mechal':85, 'Bob':89, 'Jerry':100}
print(d['Jerry'])
#为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，
#我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。

#第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字，
#无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
#这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：)
d['jerry'] = 100 #可以直接以这种方式添加
print(d['jerry'])
#如果key不存在，dict就会报错：
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Jerry' in d) #不区分大小写
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('jerry'))
print(d.get('jerry', -1))
print(d.get('wang', -1))
print(d.get('wang'))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)
#---set---
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)
#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。
#重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(33)
print(s)
#通过remove(key)方法可以删除元素：
s.remove(33)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
#str是不变对象，而list是可变对象。
#所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
'''



