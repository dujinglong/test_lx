"""
完成登录业务层实现
"""
# 导包 unittest ApiLogin
from api.api_login import ApiLogin
import unittest
import urllib3
from parameterized import parameterized
from tools.read_json import ReadJson
# 读取数据函数


def get_data():
    data = ReadJson("login.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("mobile"),
                 data.get("code"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs


# 新建测试类
class TestLogin(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self, url, mobile, code, expect_result, status_code):
        # 暂时存放数据 url mobile code
        #         # url = "https://rms.api.aixiangdao.top/rms/login"
        #         # mobile = 18321252140
        # code = "298825"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 禁止安全请求警告
        # 调用登录方法
        s = ApiLogin().api_post_login(url, mobile, code)
        # 调试使用
        print("查看响应结果: ", s.json())
        # 断言 响应信息 及状态码
        # self.assertEqual("ok", s.text)
        self.assertEqual(expect_result, s.json())
        # 断言响应状态码
        # self.assertEquals(200, s.status_code)
        # self.assertEquals(404, s.status_code)
        self.assertEqual(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()

"""
userTokend24ebb10aa-f8c2-4aee-a482-071a4115884f
"""
