#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyone.apiceshi.api.base_api import BaseApi
from pyone.apiceshi.api.wework_token import WeWork


class Address(BaseApi):
    def __init__(self):
        secret = '9nxHyqU9fU2EEuwlwUHpv5eNrd7yJbggU7stGVexmlQ'
        self.token = WeWork().get_token(secret)
    
    def get_token(self):
        # 获取通讯录的token
        secret = '9nxHyqU9fU2EEuwlwUHpv5eNrd7yJbggU7stGVexmlQ'
        return self.send(**data)["access_token"]
    
    def getuser(self, userid):
        # 根据userid查询这个成员
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        return self.send(**data)
    
    def adduser(self, userid, name, mobile, ):
        # 添加一个成员
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token": self.token},
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1],
            }
        }
        return self.send(**data)
    
    def changeuser(self, userid, name, mobile, ):
        # 更改成员的名字
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {"access_token": self.token},
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
            }
        }
        return self.send(**data)
    
    def deleteuser(self, userid, ):
        # 删除某个成员
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        return self.send(**data)
