"""
    目标：自动化测试中操作数据库
    案例：
    判断用户status状态为1 上架 0是下架

"""
# 导包pymysql
import pymysql

# 获取连接对象
conn = pymysql.connect("rm-wz91670r7o0zi042j8o.mysql.rds.aliyuncs.com",
                       "test_shanghai",
                       "shanghai@jinglong",
                       "axd_test",
                       charset="utf8"
                       )
# 获取游标对象
cursor = conn.cursor()
# 获取方法 sql
sql = "select status from axd_activity_coupon where id='34'"
cursor.execute(sql)
# 获取结果并进行断言 0 是下架
# print(cursor.fetchone())
result = cursor.fetchone()
# 断言1上架
assert 1 == result[0]
# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()