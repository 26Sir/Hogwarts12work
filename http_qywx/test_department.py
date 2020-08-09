#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def test_token():
    # 获取用户的token
    corpid = 'ww413f2cf98b9b9441'
    corpsecret = '9nxHyqU9fU2EEuwlwUHpv5eNrd7yJbggU7stGVexmlQ'
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    print(res.json())
    return res.json()["access_token"]

def test_adddepart():
    # 添加一个部门叫曹家
    data = {
            "name": "曹家",
            "name_en": "cj",
            "parentid": 1,
            "order": 1,
            "id": 2
    }
    res = requests.post(
        f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}",
        json=data
    )
    print(res.json())

def test_updatedepart():
    # 更新刚刚添加的部门曹家
    data = {
        "id": 2,
        "name": "曹家咀",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1
    }
    res = requests.post(
        f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}",
        json= data
    )
    print(res.json())
    assert res.json()["errcode"] == 0

def test_deletedepart():
    # 删除添加的部门
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id=2")
    print(res.json())
    assert res.json()["errcode"] == 0

def test_getdepart():
    # 查找现在用户下所有的部门
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}")
    print(res.json())
    assert res.json()["department"][0]["name"] == '贰六Sir'