# coding = utf-8

import requests
class Login():
    def login(self):
        headers = {"Content-Type": "application/json"}
        url = "https://pushm.api.aixiangdao.top/develop/ws/getInstance?appTag=mms&uid=18321252140&" \
              "sign=cb6ee92fee117a4c0ef260686f50bbcf"
        request = requests.get(url=url, headers=headers, verify=False)
        r = request.json()
        print(r)


if __name__ == '__main__':
    Login().login()


