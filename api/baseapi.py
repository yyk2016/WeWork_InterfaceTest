import json

import requests
#公用的方法
class BaseApi:
    params = {}
    def send(self, data):
        #json.dumps()用于将字典形式的数据转化为字符串，因为如果直接将dict类型的数据写入json文件中会发生报错
        raw_data = json.dumps(data)
        print("-----", raw_data)
        #遍历字典用items
        for key, value in self.params.items():
            raw_data = raw_data.replace("${"+key+"}", value)
        # json.loads()用于将字符串形式的数据转化为字典
        data = json.loads(raw_data)
        #**data表示解字典，因为request()有多个参数，所以需要解开字典data，将值分别传入到request()中
        return requests.request(**data).json()