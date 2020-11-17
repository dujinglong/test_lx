# 导包 requests
import requests


# 新建对象类
class ApiCity(object):
    # 新建获取频道规则
    def api_get_city(self, url, headers):
        # 调用get请求
        # return requests.get(url, headers=headers) 如果https不加上verify=False会有警告错误
        return requests.get(url, headers=headers, verify=False)
