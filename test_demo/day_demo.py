# # 既不需要侵入原函数，也不用重复调用
# import time
#
#
# def deco(func):
#     def wrapper():
#         starTime = time.time()
#         func()
#         endTime = time.time()
#         print("程序执行了{}秒".format(endTime - starTime))
#
#     return wrapper()
#
#
# # 声明myfunc是一个装饰器函数
# @deco
# def myfunc():
#     print("hello")
#     time.sleep(1)
#     print("world")
#
#
# if __name__ == '__main__':
#     f = myfunc  # 将myfunc赋值给f变量
#     f()
# 带有多个不定参数的装饰器
# import time
#
#
# def deco(func):
#     def wrapper(*args, **kwargs):
#         starTime = time.time()
#         func(*args, **kwargs)
#         endTime = time.time()
#         seconds = (endTime - starTime)
#         print("func()运行了{}秒".format(seconds))
#     return wrapper
#
# @deco
# def func(a, b):
#     print("hello,here is a fun for add:")
#     time.sleep(1)
#     print("result is {}".format(a + b))
#
# @deco
# def func2(a, b, c):
#     print("hello,here is a fun for add:")
#     time.sleep(1)
#     print("result is {}".format(a + b + c))
#
#
# if __name__ == '__main__':
#     f = func
#     func2(2, 3, 4)
#     f(3, 4)
#
# # 使用continue关键字
# a = [1, 2, 3, 4, 5]
# for i in range(len(a)):
#     # print(i)
#     continue
# else:
#     print("else")
# #
#
#
# class Person():
#     def __init__(self, name, age):
#         # 定义属性
#         self.name = name
#         self.age = age
#
#     # 定义函数
#     def say(self):
#         print('My name is {0},I am  {1} year old'.format(self.name, self.age))
#
#
# p = Person('jack', 24)
# p.say()
#
#
# a = "测试"
# b = 5
# c = a * b
# print(c)
# # 定义一个变量qq号码
# qq_number = "13392179480"
# print(qq_number)
# # 定义一个变量qq密码
# qq_password = "123456"
# print(qq_password)


# 超市买苹果
# 1、定义苹果的单价
# price = 8.5
# # 挑选苹果7.5
# weight = 7.5
# # 计算付款金额
# money = price * weight
# # 只有买苹果就返5元
# money = money - 5
# print("付款金额:", money)


"""
姓名 小明  年龄 18  性别 男  身高 1.75米   体重  75公斤
"""
# name = "小明"
# print(type("小明"))
# age = 18
# print(type(18))
# gender = True
# print(type(True))
# height = 1.75
# print(type(int(1.75)))
# weight = 75
# print(type(75))
# print(weight)

# last_name = "张"
# first_name = "三"
# number = 10
# print((last_name + first_name) * 10)
# print((last_name + "10"))
#
# password = input("请输入登录密码：")
# print(password)
# print(type(password))


# 买苹果增强版
# 1、输入苹果的单价
# price_str = input("苹果的单价: ")
# # 输入苹果的重量
# weight_str = input("苹果的重量: ")
# # 转换类型为浮点型
# price = float(price_str)
# weight = float(weight_str)
# # 计算支付的总金额
# money = price * weight
# print(money)

# 格式化字符串
# 定义变量name输出我的名字叫小明，请多多关照!
name = "刘明"
print("我的名字叫%s，请多多关照!" % name)  # %s格式化字符串

# 定义变量student_o输出学号00001
student_o = 100
print("我的学号是 %06d" % student_o)  # %后面跟几位数是显示


# 定义小数price、weight、money
price = 8.7
weight = 7.5
money = price * weight
print("苹果的单价 %.2f 元/斤,购买了 %.3f 斤，需要支付 %.4f 元" % (price, weight, money))

# 定义一个小数scale,输出数据比例是10.00%
scale = 0.8
print("输出数据比例是 %.2f%%" % (scale * 100))  # .f输出小数位，%%显示%

# 定义整数变量记录年龄
ages = int(input("请输入年龄："))
# 判断是否满18岁
if ages >= 18:
    # 判断是否满18岁欢迎来网吧嗨皮
    print("你已经成年，欢迎来网吧嗨皮！")
else:
    # 如果未满18岁，回家写作业！
    print("你未成年，回家写作业！")
# 这句代码无论条件是否满足都会执行
print("看看什么时候会执行")






