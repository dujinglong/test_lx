# 导入json
import json
from parameterized  import parameterized
# # 打开json文件并获取文件流
# with open("../data/login.json", "r", encoding="utf-8") as f:
#     # 调用load方法加载文件流
#     data = json.load(f)
#     print("获取的数据为：", data)


# def read_json():
#     # 打开json文件并获取文件流
#     with open("../data/login.json", "r", encoding="utf-8") as f:
#         # 调用load方法加载文件流
#         return json.load(f)

# 使用参数替换 动态文件名
class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        # 打开json文件并获取文件流
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载文件流
            return json.load(f)


"""
    问题：
    1、未经过封装无法在别的模块内使用
    2、数据存储文件有好几个，如果写死，在读取别的文件时无法使用
    3、预期格式为列表嵌套元组[(url, mobile,code...)]
    解决：
    1、进行封装
    2、使用参数替换静态写死的文件名
    3、读取字典的内容，并添加到新的列表中
"""

if __name__ == '__main__':
    # print(ReadJson("login.json").read_json())
    # 登录数据调试
    # data = ReadJson("login.json").read_json()
    # # 新建空列表，添加读取json数据
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("mobile"),
    #              data.get("code"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)

    # 获取频道规则
    # data = ReadJson("city.json").read_json()
    # # 新建空列表，添加读取json数据
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("headers"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)

    # 更新活动信息
    data = ReadJson("coupon.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")))
    print(arrs)
