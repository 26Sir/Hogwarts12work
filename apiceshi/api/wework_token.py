#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyone.apiceshi.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self,secret):
        # 获取通讯录的token
        corpid = "ww413f2cf98b9b9441"
        corpsecret = secret
        data = {
            "method": "get",
            "url": " https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        return self.send(**data)["access_token"]
    

