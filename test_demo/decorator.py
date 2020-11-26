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


def outer(func):
    def inner(*args, **kwargs):
        # 添加修饰的功能
        print("&&&&&&&&&&&&&&&&&&&&")
        func(*args, **kwargs)
    return inner

@outer
def say(name, age): # 函数的参数理论上是无限制的，最后不要超过6-7个
    print("my name is %s, I am %d years old" % (name, age))


say("long", 31)

