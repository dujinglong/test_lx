# 定义整数变量age, 编写代码年龄是否正确
age = 12
# 需求人的年龄0-120之间
"""
10000
age >= 0 or age <= 120
age >= 0 and age <= 120
and 
or
"""
if (age >= 0) and (age <= 120):
    print("年龄正确")
else:
    print("年龄不正确")

# 编写代码编写程序只要有60分就考试合格
python_score = 50
c_score = 50

# 需求只要有一个成绩>60分 就算合格
if python_score > 60 or c_score > 60:
    print("考试通过")
else:
    print("考试失败，继续努力")

# 定义一个布尔型变量is_employee，编写代码判断是否是本公司员工
is_employee = False

# 如果不是提示不允许入内
# 在开发中通常希望某个条件不满足时，执行一些代码，可以使用 not
# 另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到 not
if not is_employee:
    print("非本公司员工,不允许入内")


# 定义holiday_time 字符串记录节日名称   if ...elif...else
holiday_time = "生日"
# 情人节买玫瑰/看电影
if holiday_time == "情人节":
    print("买玫瑰/看电影")
# 如果是平安夜 应该买苹果/吃大餐
elif holiday_time == "平安夜":
    print("买苹果/吃大餐")
# 如果是生日应该买蛋糕
elif holiday_time == "生日":
    print("买蛋糕")
# 其他日子每天都是节日
else:
    print("每天都是节日")


# if嵌套
# 1、定义一个布尔类型变量是否有车票
has_ticket = True
# 2、定义一个变量刀的长度
knife_length = 10
# 3、检查是否有车票如果有才允许进行安检
if has_ticket:
    print("车票检查通过，准备开始安检")
    # 安检时，需要检查刀的长度，判断是否超过20厘米
    if knife_length > 20:
        # 如果超过20厘米提示刀的长度不允许上车
        print("您携带的刀太长了，有%d公分长！" % knife_length)
        print("不允许上车")
    else:
        # 如果不超过20厘米，安检通过
        print("安检已经通过，祝您旅途愉快")
# 如果没有车票，不允许通过
else:
    print("大哥，请先买票")

# 定义整数变量
i = 0
# 开始循环
while i <= 2:
    # 在循环内执行的代码
    print("hello,python")
    # 处理计算数
    i += 1
print("结束后, i = %d" % i)


# 计算0-100之间的累计求和
# result定义计算的结果
result = 0
# 计算0-100之间的累计求和
i = 0
while i <= 100:
    print(i)
    # 处理计数器
    result += i
    i += 1
print("0-100之间的累计求和 %d" % result)


# # 计算0-100之间的偶数求和
# result = 0
# i = 0
# while i <= 4:
#     if i % 2 == 0:
#         print(i)
#         # 当i这个变量是偶数时，才能累计相加
#         result += i
#     i += 1
#
# print("0~100之间的偶数加结果 = %d" % result)
#
# i = 0
# while i < 10:
#     # break某一条件达到就直接退出
#     if i == 3:
#         continue
#     print(i)
#     i += 1
# print("over")


# i = 0
# while i < 10:
#     # continue 某一条件满足时，不执行后续重复的代码
#     # i == 3
#     if i == 3:
#         # 注意在循环中使用continue这个关键字
#         # 在使用关键字之前，需要确认循环的计数是否修改
#         # 否则可能会导致死循环
#         i += 1
#         continue
#     print(i)
#     i += 1

# 用嵌套联续五行*，每一行星号的数据依次递增
# *
# **
# ***
# ****
# *****
# 1、定义计数变量，从数字1开始，循环会比较方便
row = 1
# 2、开始循环
while row <= 5:
    print("*" * row)
    row += 1

print("*", end="---")
print("*")
