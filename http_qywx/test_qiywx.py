#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def test_token():
    # 获取通讯录的token
    corpid = "ww413f2cf98b9b9441"
    corpsecret ='9nxHyqU9fU2EEuwlwUHpv5eNrd7yJbggU7stGVexmlQ'
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    print(r.json()["access_token"])
    return r.json()["access_token"]

def test_getuser():
    # 根据userid查询这个成员
    userid = 'sange'
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token()}&userid={userid}')
    print(res.json())

def test_adduser():
    # 添加一个成员
    data = {
        "userid": "sange",
        "name": "三哥",
        "mobile": "+86 13800001234",
        "department": [1],
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token()}",
                        json=data
                        )
    print(res.json())
    
def test_changeuser():
    # 更改成员的名字
    data= {
        "userid": "sange",
        "name": "三哥棒",
        "department": [1],
    }
    res = requests.post(
        f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token()}",
        json=data
    )
    print(res.json())

def test_deleteuser():
    # 删除某个成员
    userid = 'sange'
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token()}&userid={userid}")
    print(res.json())