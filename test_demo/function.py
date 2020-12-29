# import time
# from collections import Iterable
# from collections import Iterator
# 输入时分秒 23:23:23
# timeStr = input("请输入时间：")
# timeList = timeStr.split(":")  # 按照符号切割
# h = int(timeList[0])
# m = int(timeList[1])
# s = int(timeList[2])
# s += 1
# if s == 60:
#     m += 1
#     s = 0
#     if m == 60:
#         h += 1
#         m = 0
#         if h == 24:
#             h = 0
#
# print("%.2d:%.2d:%.2d" % (h, m, s))

# musicLrcList = """[00:03.50]传奇
# [00:19.10]作词：刘兵 作曲：李健
# [00:20.60]演唱：王菲
# [00:26.60]
# [04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
# [04:49.00]
# [02:47.44][00:43.69]再也没能忘掉你容颜
# [02:54.83][00:51.24]梦想着偶然能有一天再相见
# [03:02.32][00:58.75]从此我开始孤单思念
# [03:08.15][01:04.30]
# [03:09.35][01:05.50]想你时你在天边
# [03:16.90][01:13.13]想你时你在眼前
# [03:24.42][01:20.92]想你时你在脑海
# [03:31.85][01:28.44]想你时你在心田
# [03:38.67][01:35.05]
# [04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
# [04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
# [04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
# [04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
# [04:39.55][04:09.00][02:07.85]"""
# lrcDice = {}
# musicLrcList = musicLrcList.splitlines()
# gettime = 1
# # print(musicLrcList)
# for lrcLine in musicLrcList:
#     # runCount = lrcLine.count(":")
#     lrcLineList = lrcLine.split("]")  # 按照]切割
#     for index in range(len(lrcLineList)-1):  # 拿到
#         timeStr = lrcLineList[index][1:]
#         timeList = timeStr.split(":")
#         # print(timeList)
#         times = float(timeList[0]) * 60 + float(timeList[1])
#         # print(time)
#         lrcDice[times] = lrcLineList[-1]
# # print(lrcDice)
#
# allTimeList = []
# for t in lrcDice:
#     allTimeList.append(t)
# allTimeList.sort()
# print(allTimeList)
# """while 1:
#     getTime = float(input("请输入一个时间:"))
#
#     for n in range(len(allTimeList)):
#         tempTime = allTimeList[n]
#         if getTime < tempTime:
#             break
#
#         if n == 0:
#             print("时间太小")
#         else:
#             print(lrcDice[allTimeList[n - 1]])
# """
# getTime = 0
# while 1:
#     for n in range(len(allTimeList)):
#         tempTime = allTimeList[n]
#         if getTime < tempTime:
#             break
#
#     lrc = lrcDice.get(allTimeList[n - 1])
#     if lrc == None:
#         pass
#     else:
#         print(lrc)
#     time.sleep(1)
#     getTime += 1

"""
set:类似dict,是一组key的集合，不存储value
本质：无序和无重复元素的集合
"""

# 创建 set需要一个list或者tuple或者dict作为输入集合
# s1 = set([1, 2, 3, 4, 5, 3, 4, 5])
# print(s1)
#
# s2 = set((1, 2, 3, 3, 2, 1))
# print(s2)
#
# s3 = set({1: "good", 2: "nice"})
# print(s3)
#
# s4 = set([1, 2, 3, 4, 5])
# s4.add(6)
# s4.add(3) # 可以添加重复的，但是不会有效果
# # s4.add([7, 8, 9]) # set元素不能是列表，因为列表是可变的
# s4.add((7, 8, 9))
# # s4.add({1: "a"})  # set元素不能是字典，因为字典是可变的
# print(s4)
#
# # 出入整个list、update、字符串、打碎插入
# s5 = set([1, 2, 3, 4, 5])
# s5.update([6, 7, 8])
# s5.update((9, 10))
# s5.update("sunck")
# print(s5)
# # 删除
# s6 = set([1, 2, 3, 4, 5])
# s6.remove(3)
# print(s6)

# 遍历
# s7 = set([1, 2, 3, 4, 5])
# for i in s7:
#     print(i)
# set 没有索引
# print(s7[3])
# for index, data in enumerate(s7):
#     print(index, data)


# 交集
# s8 = set([1, 2, 3])
# s9 = set([2, 3, 4])
# a1 = s8 & s9
# print(a1)
# print(type(a1))
#
# # 并集
# a2 = s8 | s9
# print(a2)
# print(type(a2))


# 类型转换 a  list ->set
# list = [1, 2, 3, 4, 5]
# sets = set(list)
# print(sets)
#
#
# #  B tuple->set
# tuples = (1, 2, 3, 4)
# set1 = tuple(tuples)
# print(set1)

# c set ->lsit
# set4 = {2, 3, 4}
# list1 = list(set4)
# print(list1)

# d set ->tuple

# set5 = {2, 3, 4}
# # list2 = tuple(set4)
# # print(list2)


# list去重
# a = [1, 2, 3, 4, 3, 4, 5, 6]
# s = list(set(a))
# print(s)

# 迭代器
"""
可迭代对象：可以直接适用于for循环的对象统称为迭代对象
（Iterable）,可以用isinstance()去判读一个对象是否是可Iterable对象

可以直接作用于for的数据类型一般分两种
1、集合数据类型：如 list、tuple、 dict、set、string
2、是gengerator,包括生成器和带yield的gengerator  function

"""

# print(isinstance([], Iterable))
# print(isinstance((), Iterable))
# print(isinstance({}, Iterable))
# print(isinstance("", Iterable))
# print(isinstance((x for x in range(10)), Iterable))
# print(isinstance(1, Iterable))

'''
迭代器：不但可以用于for循环，还可被next()函数不断调用并返回下一个值，直到最后抛出StopInteration错误表示无法返回下一个值

 可以被next()函数调用不断返回下一个值的对象称为迭代器
（Iterator）
可以使用isinstance()函数判断一个对象是否是Iterator对象


'''
#
# print(isinstance([], Iterator))
# print(isinstance((), Iterator))
# print(isinstance({}, Iterator))
# print(isinstance("", Iterator))
# print(isinstance((x for x in range(10)), Iterator))
#
# l = (x for x in [23, 45, 670, 45])
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))


# 转成Iterator对象
# # a = iter([1, 2, 3])
# # print(next(a))
# print(next(a))
# print(isinstance(iter([]), Iterator))
# print(isinstance(iter(()), Iterator))
# print(isinstance(iter({}), Iterator))
# print(isinstance(iter(''), Iterator))


# 输入后必须输入end才打印
# endstr = "end"
# str = ""
# for line in iter(input, endsrt):
#     str += line + "\n"
# print(str)

"""
认识函数：在一个完整的项目中，某些功能会反复的使用。那么会将功能封装成函数，当我们要使用功能的时候直接调用函数季卡
本质：函数就是对功能的封装
优点：
1、简化代码结构，增加了代码的复用度（重复使用的程度）
2、如果想修改某些功能或者修改某个bug,还需要修改对应的函数即可

"""

"""
（参数1， 参数2， ‘’‘’‘’， 参数n）
定义函数：
格式：
def 函数名（参数列表）
    语句
    return 表达式
def:函数代码块以def关键字开始
函数名：遵循标识符规则
():是参数列表的开始和结束
冒号：函数内容（封装的功能）以冒号缩进
语句：函数封装的功能
return ：一般用于结束函数，并返回信息给函数的调用者。
表达式：即为返回给函数的调用者信息
注意：最后的return 表达式。可以不写，相当于return None
参数列表（参数1， 参数2， ‘’‘’‘’， 参数n）：任何传入函数的参数和变量必须放在圆括号之间，用逗号分隔。函数从函数的调用者哪里获取的信息
"""

"""
函数的调用
格式：函数名（参数列表）
函数名：是要使用的功能的函数名字
参数列表：函数的调用者给函数传递的信息,如果没有参数，小括号也不能省略

函数调用的本质：实参给形参赋值的过程


"""
# 凯 = "帅"
# print(凯)

# 定义了一个无参无返回的函数

#
# def myPrint():
#     print("sunck is a very good man!")
#     print("sunck is a nice man!")
#     print("sunck is a handsome man!")
#
#
# myPrint()
# myPrint()
# myPrint()


"""
函数的参数

"""


# 需求：编写一个函数，给函数一个字符串和一个年龄，在函数内部打印出来

# 形参（形式参数）：定义函数时小括号中的变量，本质是变量
# 参数必须按顺序传递，个数目前要对应
# def myPrint(str, age,hoby):
#     print(str, age)

# def myPrint(str, age):
#     print(str, age)
#
#
# # 实参（实际参数）：调用函数时传递数据，本质是值
# myPrint("sunck is a very good man!", 18)


# 编写函数，实现功能，给函数两个数，返回这2个数的和
# def mySun(num1, num2):
#     # 将结果返回给函数的调用者
#     return num1 + num2
#     # 执行完return语句，该函数就结束了，return后面的代码不会执行
#     print("**********")
#
#
# res = mySun(1, 2)
# print(res)



# 传递参数

"""
值传递：传递不可变类型
string、tupel、number
"""
# def fun1(num):
#     num = 10
#
# temp = 20
# fun1(temp) # num = temp
# print(temp)

"""
引用传递：传递可变类型
list、 dict、set是可变的
"""

#
# def func2(lis):
#     lis[0] = 100
# li = [1, 2, 3, 4,5]
# func2(li)
# print(li)
#
# a = 10
# b = 10
# print(id(a), id(b))
#
# c = 20
# d = 30
# print(id(c), id(d))
# d = c
# print(id(c), id(d))



"""
概念：允许函数调用时参数的顺序与定义时不一致

"""

#
# def myPrint(str, age):
#     print(str, age)
#
#
# # 使用关键字参数
# myPrint(age=18, str="sunck is a good man")



"""
概念：调用函数时，如果没有传递参数，则使用默认参数

"""


# 以后要用默认参数，最好将默认参数放到最新
# def myPrint(str, age=18):
#     print(str, age)
#
#
# # 使用关键字参数
# myPrint("kaige good")


"""
概念：能处理比定义时更多的参数
"""
# 加了星号（*）的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元组


# def func(name, *arr):
#     print(name)
#
#     for x in arr:
#         print(x)
#
#
# func("sunck", "good", "nice", "handsom")

# def mySun(*l):
#     sum = 0
#     for i in l:
#         sum += i
#     return sum
#
#
# print(mySun(1, 2, 3, 4, 5, 6))

# **代表键值对的参数字典，和*所代表的意义类似
# def func2(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
#
# func2(x=1, y=2, z=3)  # 打印出字典： {'x': 1, 'y': 2, 'z': 3}
# # func2(1, 2, 3)  # 报错
#
# 不定长函数
# def func3(*args, **kwargs):
#     pass  # 代表一个空语句


"""
匿名函数：不使用def这样的语句定义函数，使用lambda来创建匿名函数
特点：
1、lambda 只是一个表达式，函数体比def简单
2、lambda 的主体是一个表达式，而不是代码块，仅仅只能在lambda表达式中封装简单的逻辑
3、lambda函数有自已的命名空间，切不能访问自由参数列表之外的或全局命名空间的参数
4、虽然lambda 是一个表达式且看起来只能写一行，与c和c++内联函数不同

格式：
lambda 参数1， 参数2，....,参数n：expression
"""
#
# sum = lambda num1, num2: num1+num2
# print(sum(1, 2))

# 什么是函数：函数就是一段事先组织好的，它具有可重复性，封装好，用来实现某个相关联功能的代码段，函数能提高应用的模块性，
# 和代码的重复利用率。

# 未携带函数格式


def name():  # name
    print('这是一个函数')
    return name


name()

# 携带从参数函数格式


def name(name):
    print('这是函数名', name)
    return name


name('name')
'''
通常来说函数必须要遵循以下几点：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
圆括号之间可以用于定义参数。
函数内容以冒号起始，并且缩进。
return 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''
# 可变与不可变

# 不可变参数
def name(a):
    a = 20
    print(a)


b = 10
name(b)  # 20
print(b)  # 10

# 可变参数


def changme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值", mylist)  # [10, 20, 30, [1, 2, 3, 4]]
    return


# 调用函数
mylist = [10, 20, 30]
changme(mylist)
'''
不可变：整数、字符串、元组
可变参数：字典，列表
'''

# 全局变量和局部变量：定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域，局部变量只能在其被声明的函数内部访问，
# 而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
name = 'jinglong'


def name_01(name):
    print('现在我的名字是：', name)  # jinglong
    name = 'test'
    print('现在我的名字是：', name)  # test


name_01(name)
print('外面我的名字是：', name)  # jinglong

# 函数之前的调用


def jiafa(a, b):
    # 加法
    c = a + b
    return c


def jianfa(c):
    d = 2
    s = c - 2
    print(s)


c = jiafa(2, 5)  # 调用函数加法
jianfa(c)  # 调用函数减法


# 非固定函数：若你的函数在定义时不确定用户想传入多少个参数，就可以使用非固定参数，引入*args,**kwargs
def name(name, *args):
    print(name, args)  # Jinglong ('test', 123)


name('Jinglong', 'test', 123)  # Jinglong ('test', 123) 这个时候会发现*args 传入的内容会变成一个元祖


def name(name, **kwargs):
    print(name, kwargs)


name('jinlgong', it='test', age=32)  # jinlgong {'it': 'test', 'age': 32} 这个时候会发现**kwargs传入的内容会变成一个字典

# 递归：函数之间可以进行调用，那么函数本身也可以进行调用，这种函数我们叫做递归


def calc(n):
    print(n)
    if int(n/2) == 0:
        return n
    return calc(int(n/2))


calc(10)  # 10  5 2 1
