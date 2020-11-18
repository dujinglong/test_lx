# 导包
import unittest
from api.api_coupon_insert import ApiCouponInsert
from tools.read_json import ReadJson
from parameterized import parameterized
import urllib3


def data():
    # 更新活动信息
    data = ReadJson("coupon.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs


# 创建上架活动类
class Testcoupon(unittest.TestCase):
    """测试活动管理"""
    @parameterized.expand(data())
    # 定义测试方法
    def test_coupon(self, url, headers, data, expect_result, status_code):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # 暂时存放数据
        # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # url = "https://rms.api.aixiangdao.top/activity/activity/coupon/update"
        # headers = {"Content-Type": "application/json; charset=utf-8", "branch": "develop",
        #            "userToken": "28d978b7c-2743-4bb5-8c6d-5d65a4718ed9"}
        # data = {"id": 34, "status": 1}
        r = ApiCouponInsert().api_post_insert(url, headers, data)
        print("响应结果：", r.json())
        # 断言 接口返回状态
        self.assertEqual(status_code, r.status_code)
        # 断言 返回的响应结果
        self.assertEqual(expect_result, r.json()['data'])


if __name__ == '__main__':
    unittest.main()


