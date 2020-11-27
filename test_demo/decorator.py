"""
装饰器概念：是一个闭包，把一个函数当做参数返回一个替代版的函数，本质上就是一个返回函数的函数
"""


# # 简单的装饰器
# def func1():
#     print("sunck is a goog man")
#
#
# def outer(func):
#     def inner():
#         print("******")
#         func()
#     return inner
#
#
# # f 是函数func1的加强版本
# f = outer(func1)
# f()

# def say(age):
#     print("sunck is a %d years old" %(age))

# say(-10)

# 复杂一点装饰器
# def outer(func):
#     def inner(age):
#         if age < 0:
#             age = 0
#         func(age)
#     return inner
#
# # 使用@符合将装饰器应用到函数
# # @python2.4支持使用@符合
# @outer
# def say(age):
#     print("sunck is a %d years old" %(age))
# # says = outer(say)
#
#
# say(-10)


"""
通用装饰器
"""


# def outer(func):
#     def inner(*args, **kwargs):
#         # 添加修饰的功能
#         print("&&&&&&&&&&&&&&&&&&&&")
#         func(*args, **kwargs)
#     return inner
#
# @outer
# def say(name, age): # 函数的参数理论上是无限制的，最后不要超过6-7个
#     print("my name is %s, I am %d years old" % (name, age))
#
#
# say("long", 31)
import functools

"""
偏函数
"""
# print(int("1010", base=2))
# def int2(str,base=2):
#     return int(str, base)
#
# print(int2("1011"))

# 把一个参数固定住，形成一个新的函数
# int3 = functools.partial(int, base=2)
# print(int3("110"))

"""
变量的作用域
作用域：变量可以使用的范围
程序的变量并不是所有的位置都能使用的，访问的权限决定于变量在哪里赋值
作用域：
局部作用域
全局作用域

"""
# try:
#     print(3/1)
#     # print(num)
# except NameError as e:
#     print("没有该变量")
# except ZeroDivisionError as e:
#     print("除数为0了")
# else:
#     print("代码没有问题")
# print("*********")
# 需求：当程序预定问题不让程序结束，而越过错误向下执行

"""
try......except.........else
格式：
try:
    语句t
expect 错误码 as e:
    语句1

expect 错误码 as e:
    语句2
...
expect 错误码 as e:
    语句n
else:
    语句e
注意：else语句可有可无
作用：用例检测try语句块中的错误，从而让except语句捕获错误信息并处理
逻辑：单程序执行到try-except-else语句
1、如果当try"语句t"执行出现错误,会匹配第一个错误码如果匹配上就执行对应的“语句”
2、如果当try"语句t"执行出现错误,没有匹配的异常，错误将会被提交到上一层的try语句。或者到程序的最上层
3、如果当try"语句t"执行没有出现错误，执行else下的“语句”（你得有）

"""


# 使用expect而不是使用任何的错误类型

# try:
#     # print(4/0)
#     print(num)
# except:
#     print("程序出现了异常")

#  使用tryexcept带着多种异常错误处理

# try:
#     print(4/0)
# except (NameError, ZeroDivisionError):
#     print("出现了NameError或ZeroDivisionError")

# 特殊
# 1、错误其实是class(类),所有的错误都继承BaseException，所以在捕获的时候，它捕获了该类型错误，还把子类一网打尽
# try:
#     print(5/0)
# except BaseException as e:
#     print("异常1")
# except ZeroDivisionError as e:
#     print("异常2")


# 跨越多层调用,main调用了func2,func2调用了func1，func1出现了错误
# def func1(num):
#     print(1 / num)
#
#
# def func2(num):
#     func1(num)
#
#
# def main():
#     func2(0)
#
#
# try:
#     main()
# except ZeroDivisionError as e:
#     print("***")

"""
try...except...finally
格式：
格式：
try:
    语句t
expect 错误码 as e:
    语句1

expect 错误码 as e:
    语句2
...
expect 错误码 as e:
    语句n
finally:
    语句f
作用：语句t无论是否有错误都执行最后的语句f
"""
# try:
#     print(5/0)
# # except BaseException as e:
# #     print("为0了")
# finally:
#     print("必须执行我")

'''
assert:可作为调试信息
'''


def func(num, div):
    assert(div != 0), "div不能为0"
    return num/div


print(func(10, 0))  # AssertionError: div不能为0

