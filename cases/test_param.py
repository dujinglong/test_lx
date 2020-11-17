"""
    目标：回顾parameterized参数化组件使用
    安装：pip install parameterized
    使用：@parameterized.expand(参数)
    参数：
        单个参数格式：列表 如：[值1，值2]
        多个参数：列表嵌套元组： 如[参值1，参值2]
    需求：
        输出用户名和密码，数据分别为 1.18321252140 , 123456 2. 1339217480 217480
"""

# 导包
import unittest
from parameterized import parameterized
# 新建测试类


class TestPara(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand([("18321252140", "123456"), ("1339217480", "217480")])
    def test_para(self, username, password):
        print("用户名：" + username)
        print("密码：" + password)

