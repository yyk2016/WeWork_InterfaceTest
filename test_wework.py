import random
import pytest
import requests
from requests import session

def test_create_data():
    #列表生成器,userid,name,mobile
    #data = [(str(random.randint(0, 99999)), "柯南", str(random.randint(13300000000, 13399999999))) for x in range(3)]
    data = [("kenanxxxx" + str(x), "xiaoyu", "1375%07d" % x) for x in range(3)]
    print(data)
    return data

class TestWework:
        @pytest.fixture(scope="session")
        def token(self):
            request_params = {
                "corpid": "wwbdeb75111f687ad7",
                "corpsecret": "tEz6Uj5hPss0LgtsCAu9DAIR0Bq412Xz2dYWz_v6Pow"
            }
            r = requests.get(
                "https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_params)
            return r.json()['access_token']

        def test_get_token(self):
            """
            获取token
            https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
            :return:
            """
            r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwbdeb75111f687ad7&corpsecret=tEz6Uj5hPss0LgtsCAu9DAIR0Bq412Xz2dYWz_v6Pow")
            #print(r.json()['access_token'])
            return r.json()['access_token']
#创建成员
        def test_create(self, token, userid, name, mobile, department=None):
            """
            创建成员
            https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
            :return:
            """
            #access_token = self.test_get_token()
            if department is None:
                department = [1]
            request_body = {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
            }
            # print('====',request_body)
            r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",json=request_body)
            print(r.json())
            return r.json()

#读取成员
        def test_get(self,token):
            """
            获取成员
            https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
            :return:
            """
            #access_token = self.test_get_token()
            #r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid=LaLa")
            r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/list_id?access_token={token}")
            print(r.json())

#更新成员
        def test_update(self,token, userid, name, mobile):
            """
            更新成员
            https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
            :return:
            """
            #access_token = self.test_get_token()
            request_body = {
                "userid": userid,
                "name": name,
                "mobile": mobile
                #"department": [1]
            }
            r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}", json=request_body)
            # print(r.json())
            return r.json()
#删除成员
        def test_delete(self,token, userid):
            """
            删除成员
            https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
            :return:
            """
            #access_token = self.test_get_token()
            r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
            return r.json()


        @pytest.mark.parametrize("userid, name, mobile", test_create_data())
        def test_wework(self, token, userid, name, mobile):
            """
            集成测试
            :return:
            """
            # list=test_create_data()
            # for i in list:
            #     userid, name, mobile = i[0] ,i[1], i[2]
            #print('000000000')
            self.test_create(token, userid, name, mobile)
            #assert "created" == self.test_create(token, userid, name, mobile)["errmsg"]
            #self.test_update(token, "70193", "哈哈")
            #self.test_delete(token, "kenan123")

