# coding = utf-8

import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
url = "https://pushm.api.aixiangdao.top/develop/ws/getInstance?appTag=mms&uid=18321252140&sign=cb6ee92fee117a4c0ef260686f50bbcf"
requests = requests.get(url=url, headers=headers)
requests.text()

