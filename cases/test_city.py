# 导包 unittest ApiCity
import unittest
from api.api_city import ApiCity
from parameterized import parameterized
from tools.read_json import ReadJson
import urllib3


def get_data():
    # 获取频道规则
    data = ReadJson("city.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs


# 新建测试类 继承
class TestCity(unittest.TestCase):
    """用例说明：测试城市"""
    @parameterized.expand(get_data())
    # 新建测试方法
    def test_city(self, url, headers, expect_result, status_code):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 禁止安全请求警告
        # 临时数据
        # url = "https://rms.api.aixiangdao.top/basic/queryCityName?cityId=-1"
        # headers = {"Content-Type": "application/json; charset=utf-8", "branch": "develop",
        # "userToken": "28d978b7c-2743-4bb5-8c6d-5d65a4718ed9"}
        # 调用获取城市频道列表方法
        r = ApiCity().api_get_city(url, headers)
        # 调试信息，打印响应结果
        # responese = r.json()
        print("查看响应信息：", r.json())

        # 断言 状态码
        # self.assertEqual(200, r.status_code)

        # 断言 使用参数化
        self.assertEqual(status_code, r.status_code)
        # 断言 响应信息
        # self.assertTrue("深圳市" in r.text)


if __name__ == '__main__':
    unittest.main()


