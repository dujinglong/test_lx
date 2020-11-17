# if...else的使用格式
# age = 18
# if age >= 18:
#     print("可以学车了")
# else:
#     print("不可以学车")

# if...elif...else使用
# age = 10
# if age >= 18:
#     print("可以上大学了！")
# elif age > 3:
#     print("可以上幼儿园了！")
# else:
#     print("可以上小学")


# if嵌套使用格式
# ticket = 1
# knift = 10
#
# if ticket == 1:
#     print("可以坐火车")
#     if knift < 10:
#         print("通过安检")
#         print("终于可以去旅游了！")
#     else:
#         print("安检未通过")
#         print("带的水果刀超过标准")
# else:
#     print("没有通过，不能进站")
#     print("可以去旅游了！")

# while的使用格式
# n = 10
# sum = 0
# counter = 1
# while counter < n:
#     sum = sum + counter
#     counter += 1
# print("1到%d之和为： %d" %(n, sum))
#
# # while...else使用
# count = 0
# while count < 5:
#     print(count, "小于5")
#     count = count + 1
# else:
#     print(count, "大于或等于5")

# a = 1
# while a < 10:
#     print(a)
#     a += 2

# 列表
# list = ['long', 'du', 'wei', 'yan']
# print(list[1])  # 索引访问列表的值
# list.append('liu')  # 添加指定元素在末尾
# print(list)
# list.insert(1, 'only')  # 插入指定元素位置
# print(list)
# list.remove('yan')  # 删除指定元素
# print(list)

# 切片
# str_list = [3, 4, 5, 6, 7, 8, 9]
# new_1 = str_list[1:3]  # 从索引1取到索引3
# new_2 = str_list[0:6:2]  # 从索引0开始取，每两位一取，到第6位为止
# new_3 = str_list[-2:]  # 取后面2个数
# new_4 = str_list[:3]  # 取前面3个数
# new_5 = str_list[::3]  # 取所有数，每3个取一个
# print(new_1, new_2, new_3, new_4, new_5)  # [4, 5] [3, 5, 7] [8, 9] [3, 4, 5] [3, 6, 9]
#
# # 元组
# age = (18, 25, 33)
# print(age)
# age = tuple((18, 25, 33))
# print(age)
#
# # 字典
# phone = {"张三": '13099589454',
#          "李四": '18189569956',
#          "王五": '18583848349'
#         }
# print(phone['张三'])
# phone.pop('张三')  # 删除张三
# print(phone)
# phone.popitem() # 随机删除某一个
# print(phone)

# # 遍历
# for key in phone:
#     print(key, phone[key])  # 张三 13099589454 李四 18189569956 王五 18583848349
#
# # for...in循环
# num = []
# for i in range(10):
#     num.append(i)
# print(num)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # 用户交互
# name = input('请输入您的姓名：')
# height = input('请输入您的身高：')
# print('%s的身高%s厘米' % (name, height))

# 读取文件
# f = open(r'D:\test_jmt\Tk_plus.txt', 'r')
# print(f.read())  # 读取文件全部内容
# for line in f.readlines():  # readlines()读取整个文件，并按行存进列表
#     print(line.strip('\n'))  # 去掉尾行的\n
# while 1:
#     line = f.readline()  # readline()每次只读取一行
#     print(line.strip('\n'))
#     if not line:
#         break
# f.close()

# 写文件+读取文件内容
# f = open(r'D:\test_python.txt', 'a')
# f.write('hello word! \n')
# f.close()
# fp = open(r'D:\test_python.txt','r')
# print(fp.read())

'''1、用python3写出九九乘法表'''
for i in range(1, 10):
    for j in range(1, i+1):
        s = i * j
        print('%d*%d=%d\t' % (i, j, s), end='')
    print("")  # 换行

'''2.使用类似三目运算符的方式来实现一个数的绝对值 if else'''
# # 输入一个数，然后利用一个语句求它的绝对值
# num = int(input("请输入一个整数："))
# # num_abs = num if num > 0 else -num
# # print(num_abs)
# # 输入一个数复合条件判断的使用(1<num<=5)
# if 0 <= num <= 100:
#     print("这个数在0~100之间")
# else:
#     print("这个数不在0~100之间")  # 请输入一个整数：100 这个数在0~100之间
#
# '''3、字符和Unicode编码之间的转换'''
#
# n = int(input("请输入一个(0~65535)："))
# print(n, "对应的字符是：", chr(n))
# ch = input("请输入一个字符：")
# print(ch, "对应的Unicode码数为", ord(ch))
#
# '''4、判断是否是回文字符串,类似这种"abcba"'''
# s = input("请输入一个字符串:")
# # 使用切片的方式实现字符串的翻转
# s1 = s[::-1]

# 如果翻转之后的字符串和原来的字符串相等，则是回文.
# if s == s1:
# #     print("{}是回文数".format(s))
# # else:
# #     print("{}不是回文数".format(s))

'''5、判断100到999之间的水仙花数,水仙花数是指个位的三次方,十位的三次方和百位的三次方的和等于自身'''
# 水仙花数的计算（100到999）
# 先使用笨方法，将这个数的个十百提取出来


def isWenterNumber(n):
    # 个位，对10求余
    a = n % 10
    # 十位，对100求余数，然后地板除10
    b = (n % 100) // 10
    # 百位，直接对应100的除
    c = n // 100
    # 判断条件，如果满足条件就返回True
    return a ** 3 + b ** 3 + c ** 3 == n


def isNumber(n):
    # 利用字符串，字符串三个元素就是对应了个十百位上的数
    s = str(n)
    return int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3 == n


if __name__ == '__main__':
    for x in range(100, 1000):
        if isNumber(x):
            print("水仙花数为：", x)  # 水仙花数为： 153 水仙花数为： 370 水仙花数为： 371 水仙花数为： 407


'''6、按照行数答应100以内的素数，利用函数'''


def isPrine(n):
    if(n < 2):
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def printPrime():
    for x in range(101):
        if isPrine(x):
            print(x, end=" ")
    print()


if __name__ == '__main__':
    printPrime()   # 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
#
# put = input("请输入：")
# count = put.split()
# print(count)
# c = count[0]
# for j in range(len(count) - 1):  # 90 340 348 263 495
#     print(j)
#     for c in range(j + 1, count):
#         if c > count[j + 1]:
#             c = c
# print(c)

# 问题:编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上
# 提示:考虑使用range(#begin， #end)方法
ls = []
for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        ls.append(str(i))
print(','.join(ls))  # 2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,
# 2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,
# 2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,
# 2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,
# 2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,
# 2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073
# ,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199


# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
number = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (j != k) and (k != i):
                print(i, j, k)
                number += 1
print(number)   # 24   # 具体数字： 1 2 3  1 2 4  1 3 2  1 3 4  1 4 2  1 4 3  2 1 3  2 1 4  2 3 1  2 3 4  2 4 1  2 4 3  3 1 2
# 3 1 4  3 2 1  3 2 4  3 4 1  3 4 2  4 1 2  4 1 3  4 2 1  4 2 3  4 3 1  4 3 2


# 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# a = input('被加数字: ')
# b = int(input('加几次：'))
# res = 0
# for i in range(b):
#     res += int(a)
#     a += a[0]
# print('结果是：', res)

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
high = 200
total = 100
for i in range(10):
    high /= 2
    total += high
    print(high / 2)
print('总长：', total)  # 299.8046875

# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
peach = 1
for i in range(9):
    # print('i=', i)
    peach = (peach + 1) * 2
print(peach)

# 统计 1 到 100 之和
res = 0
for i in range(1, 101):
    # print(i)
    res += i
print(res)  # 1到10之和为：55

# while的使用
# a = 1
# while a < 5:
#     print(a)
#     a += 2
n = 10
numbers = 0
s = 1
while s <= n:
    numbers = numbers + s
    s += 1
print('1到%d之和为：%d' % (n, numbers))
nums = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(nums) > 0:
    summer = nums.pop()
    if summer % 2 == 0:
        even.append(summer)
    else:
        odd.append(summer)
print(even)  # [8, 42, 12]
print(odd)  # [3, 5, 37]

# 1. 将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表。
conut= list((1, 2, 3)) + list({4, 5, 6})
print(conut)

# 2. 在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0
list1 = [1, 2, 3, 4, 2, 6, 4]
list1.insert(0, 7)
list1.append(0)
l2 = list(set(list1))  # 删除重复元素
print(list1)
print(l2)

# 输入某年某月某日，判断这一天是这一年的第几天？
# import datetime
# y = int(input("请输入4位数字的年份："))
# m = int(input("请输入月份："))
# d = int(input("请输入是哪一天："))
# getDay = datetime.date(y, m, d)
# dayCount = getDay - datetime.date(getDay.year - 1, 12, 31)
# print("%s是 %s 年的第%s。" % (getDay, y, dayCount.days))


# 用一行代码生成[1,4,9,16,25,36,49,64,81,100]
print([x * x for x in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 十进制转二进制、八进制、十六进制
# dec = int(input("输入数字："))
# print("十进制为：", dec)
# print("转二进制为：", api(dec))
# print("转八进制为：", oct(dec))
# print("转十六进制为：", hex(dec))

# 生成日历
# import calendar
# yy = int(input("输入年份:"))
# mm = int(input("输入月份:"))
# print(calendar.month(yy, mm))

# 打印每个名字
name = ["Johan", "Men", "Xin", "HanMeiMei"]
for i in range(len(name)):
    print("Hello, %s" % name[i])

# 计算平方根
num = float(input('请输入一个数字：'))
num_sqrt = num ** 0.5
print('%0.2f 的平方根为 %0.2f' % (num, num_sqrt))
print("Hello", "你好！")
print("Hello", "你！")
print("Hello")