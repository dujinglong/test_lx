"""
实现登录接口对象封装
"""
# 导包
import requests


# 新建类 登录接口对象
class ApiLogin(object):
    # 新建方法 登录方法
    def api_post_login(self, url, mobile, code):
        # # headers 定义
        headers = {"Content-Type": "application/json; charset=utf-8", "branch": "develop"}
        # data 定义
        data = {"mobile": mobile, "verifyCode": code}
        # 调用post并返回响应对象
        return requests.post(url, headers=headers, json=data, verify=False)

"""

url, mobile, code:最后都是要从data中文件读取出来，做参数化使用，所以这里我们动态传参

"""