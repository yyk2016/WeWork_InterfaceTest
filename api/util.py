import requests
class Util:
    def get_token(self):
        """
        获取token
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwbdeb75111f687ad7&corpsecret=tEz6Uj5hPss0LgtsCAu9DAIR0Bq412Xz2dYWz_v6Pow")
        # print(r.json()['access_token'])
        return r.json()['access_token']