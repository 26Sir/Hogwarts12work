#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import random
import pytest
import requests

@pytest.fixture(scope="session")
def test_token():
    res = None
    # 获取通讯录的token
    corpid = "ww413f2cf98b9b9441"
    corpsecret ='9nxHyqU9fU2EEuwlwUHpv5eNrd7yJbggU7stGVexmlQ'
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    return res.json()["access_token"]

def test_getuser(userid,test_token):
    # 根据userid查询这个成员
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}')
    return res.json()

def test_adduser(userid, name, mobile,test_token):
    # 添加一个成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1],
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",
                        json=data
                        )
    return res.json()
    
def test_changeuser(userid, name, mobile,test_token):
    # 更改成员的名字
    data= {
        "userid": userid,
        "name": name,
        "mobile":mobile,
        "department": [1],
    }
    res = requests.post(
        f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",
        json=data
    )
    return res.json()

def test_deleteuser(userid,test_token):
    # 删除某个成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return res.json()
    
def test_add_date():
    # data = [(str(random.randint(0, 9999999)),
    #             "zhangsna",
    #             str(random.randint(13800000001,13800009999))) for x in range(10)]
    data = [(吃 % x) for x in range(20)]
    return data

@pytest.mark.parametrize("userid, name, mobile",test_add_date())
def test_all(userid, name, mobile,test_token):
    # 可能创建失败
    
    try:
        assert "created" == test_adduser(userid,name,mobile,test_token)['errmsg']
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            # 如果手机号被使用了，找出使用手机号的userid，进行删除
            re_userid = re.findall(":(.*)'$",e.__str__())[0]
            if re_userid.endswith("'") or re_userid.endswith('"'):
                re_userid = re_userid[:-1]
            assert "deleted" == test_deleteuser(re_userid,test_token)['errmsg']
            assert 60111 == test_getuser(re_userid,test_token)['errcode']
            assert "created" == test_adduser(userid, name, mobile,test_token)['errmsg']
            
    # 可能发生userid不存在的异常
    assert  name == test_getuser(userid,test_token)['name']
    assert "updated"==test_changeuser(userid,"xxxx",mobile,test_token)['errmsg']
    assert "xxxx" == test_getuser(userid,test_token)['name']
    assert "deleted" == test_deleteuser(userid,test_token)['errmsg']
    assert 60111 == test_getuser(userid,test_token)['errcode']
