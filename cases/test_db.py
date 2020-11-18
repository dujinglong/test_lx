"""
    目标：在unittest框架中使用数据库工具类
"""
# 导包
import unittest
from tools.read_db import ReadDB


# 新建测试类 继承
class TestDB(unittest.TestCase):
    # 新将测试方法
    def test_db(self):
        # 定义sql
        sql = "select status from axd_activity_coupon where id='34'"
        # 调用 get_sql_one 方法
        data = ReadDB().get_sql_one(sql)
        # 调试
        print(data)
        # 断言
        self.assertEquals(1, data[0])


if __name__ == '__main__':
    unittest.main()
