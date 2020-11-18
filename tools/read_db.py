"""
    目标：完成数据库工具类封装
    1、主要方法
        假设：def get_sql_one(sql)
    2、辅助方法
        1、获取连接对象
        2、获取游标对象
        3、关闭游标对象方法
        4、关闭连接对象方法

"""
# 导包 pymysql
import pymysql


# 新建工具类 数据库
class ReadDB:
    # 定义连接对象 类方法
    conn = None
    # 获取连接对象方法封装

    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect("rm-wz91670r7o0zi042j8o.mysql.rds.aliyuncs.com",
                                        "test_shanghai",
                                        "shanghai@jinglong",
                                        "axd_test",
                                        charset="utf8")
        # 返回连接对象
        return self.conn

    # 获取游标对象方法封装
    def get_cursor(self):
        return self.get_conn().cursor()

    # 关闭连接对象方法封装
    def close_cursor(self, cursor):
        if cursor:
            cursor.close()

    # 关闭游标对象方法封装
    def close_conn(self):
        if self.conn:
            self.conn.close()
            # 注意：关闭连接对象后，对象还存在内存中，需要手动设置为None
            self.conn = None

    # 主要执行方法 在外界调用方法就可以完成数据库相应操作
    def get_sql_one(self, sql):
        # 定义游标对象及数据变量
        sursor = None
        data = None
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 调用方法
            sursor.execute(sql)
            # 获取结果
            data = sursor.fetchone()
        except Exception as e:
            print("get_sql_one error:", e)
        finally:
            # 关闭游标对象
            self.close_cursor(sursor)
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data

    # 获取 所有数据库结果集
    # def get_sql_all(self, sql):
    #     sursor = None
    #     data = None
    #     try:
    #         # 获取游标对象
    #         sursor = self.get_cursor()
    #         # 调用方法
    #         sursor.execute(sql)
    #         # 获取所有结果
    #         data = sursor.fetchall()
    #     except Exception as e:
    #         print("get_sql_one error:", e)
    #     finally:
    #         # 关闭游标对象
    #         self.close_cursor(sursor)
    #         # 关闭连接对象
    #         self.close_conn()
    #         # 返回执行结果
    #         return data
    #
    # # 修改、删除、新增
    # def updata_sql(self, sql):
    #     sursor = None
    #     data = None
    #     try:
    #         # 获取游标对象
    #         sursor = self.get_cursor()
    #         # 调用方法
    #         sursor.execute(sql)
    #         # 提交事务
    #         self.conn.commit()
    #     except Exception as e:
    #         # 事务回滚
    #         self.conn.rollback()
    #         print("get_sql_one error:", e)
    #     finally:
    #         # 关闭游标对象
    #         self.close_cursor(sursor)
    #         # 关闭连接对象
    #         self.close_conn()

