import random
# 注意：在导入工具包，应该减导入语句，放在顶部
# 因为
# 1、从控制台输入要出的拳--（1）剪刀 (2)布 (3)石头
# 2、电脑随机出拳
# 3、比较胜负
#  石头 胜 剪刀
# 剪刀 胜 布
# 布 胜 石头
player = int(input("请输入你要出的拳（1）石头 (2)剪刀 (3)布"))
print("玩家选择的拳头是 %d" % player)
# computer = 3
computer = random.randint(1, 3)
print("玩家选择的拳头是 %d - 电脑出的拳是 %d" % (player, computer))
# 3、比较胜负
#  石头 胜 剪刀 if or or or
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("欧耶，电脑弱爆了")
# 平局
elif player == computer:
    print("真是心有灵犀，再来一盘")

# 其他情况电脑胜利
else:
    print("不服气，我们决战到天明")

