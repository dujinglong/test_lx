# 导包 requests
import requests


# 新建活动信息类
class ApiCouponInsert():
    # 新建活动信息方法
    def api_post_insert(self, url, headers, data):
        # 调用 post方法并返回响应
        return requests.post(url, headers=headers, json=data, verify=False)

    # def api_delete_insert(self, url, headers, data):
    #     # 调用 post方法并返回响应
    #     return requests.post(url, heasers=headers, json=data, verify=False)
