import requests
from ..api.util import Util
from ..api.baseapi import BaseApi
import yaml

class WeWork(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
    # 创建成员
    def test_create(self, userid, name, mobile, department=None):
        """
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        # access_token = self.test_get_token()
        if department is None:
            #department = [1]
            department = "1"
        # request_body = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": department
        # }
        # print('====',request_body)
       # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}", json=request_body)
       #  data = {
       #      "method": "post",
       #      "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
       #      "json": {
       #      "userid": userid,
       #      "name": name,
       #      "mobile": mobile,
       #      "department": department}
       #  }
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        self.params["department"] = department
        with open("api/wework.yaml", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        return self.send(data["create"])
        # print(r.json())
        # return r.json()

    # 读取成员
    def test_get(self):
        """
        获取成员
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # access_token = self.test_get_token()
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid=LaLa")
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/list_id?access_token={self.token}")
        print(r.json())

    # 更新成员
    def test_update(self, userid, name):
        """
        更新成员
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        # access_token = self.test_get_token()
        # request_body = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile
        #     # "department": [1]
        # }
        #r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}", json=request_body)
        # print(r.json())
        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #     "json": {
        #         "userid": userid,
        #         "name": name,
        #         }
        # }
        #return r.json()
        self.params["userid"] = userid
        self.params["name"] = name
        with open("api/wework.yaml", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            print("-------", data)
        return self.send(data["update"])

    # 删除成员
    def test_delete(self, userid):
        """
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # access_token = self.test_get_token()
        #r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")
        #return r.json()
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}",
            "json": {
                "userid": userid

            }
        }

        return self.send(data)