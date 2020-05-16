#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_wxlogin:
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9226"
        self.driver = webdriver.Chrome()
    
    def teardown(self):
        self.driver.quit()
    
    def test_login(self):
        cookies = [
            {'domain': '.qq.com', 'expiry': 1589620137, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
                             'secure': False, 'value': '1688850719731427'}, {'domain': '.work.weixin.qq.com',
                                                                             'httpOnly': False, 'name': 'wxpay.vid',
                                                                             'path': '/', 'secure': False,
                                                                             'value': '1688850719731427'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
                'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/',
                                'secure': False, 'value': 'a76561'}, {'domain': '.work.weixin.qq.com',
                                                                      'httpOnly': False,
                                                                      'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
                                                                      'path': '/', 'secure': False,
                                                                      'value': '1589618520'}, {'domain': '.qq.com',
                                                                                               'expiry': 1619744450,
                                                                                               'httpOnly': False,
                                                                                               'name': 'ied_qq',
                                                                                               'path': '/',
                                                                                               'secure': False,
                                                                                               'value': 'o1735339370'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
                'value': '21448469592519636'}, {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey',
                                                'path': '/', 'secure': False, 'value': '3020757825'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                'value': 'M6nJDSA4PO5tKf3xRcuhD7oof1EED30miAt_78reX4dxylZyMrhDgQPoQoUgm8Eo'}, {'domain': '.qq.com',
                                                                                               'expiry': 1589705780,
                                                                                               'httpOnly': False,
                                                                                               'name': '_gid',
                                                                                               'path': '/',
                                                                                               'secure': False,
                                                                                               'value': 'GA1.2.1723417234.1589617574'}, {
                'domain': '.qq.com', 'expiry': 1652691380, 'httpOnly': False, 'name': '_ga', 'path': '/',
                'secure': False, 'value': 'GA1.2.1150673087.1586019624'}, {'domain': '.work.weixin.qq.com',
                                                                           'expiry': 1592212080,
                                                                           'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                                                                           'path': '/', 'secure': False,
                                                                           'value': 'zh'}, {'domain': '.qq.com',
                                                                                            'expiry': 1608727326,
                                                                                            'httpOnly': False,
                                                                                            'name': 'eas_sid',
                                                                                            'path': '/',
                                                                                            'secure': False,
                                                                                            'value': 'F1a5E7m7G139h1S3z2s6o2A322'}, {
                'domain': '.qq.com', 'expiry': 1617555625, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/',
                'secure': False, 'value': '1586019625'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                                                          'name': 'wwrtx.ref', 'path': '/', 'secure': False,
                                                          'value': 'direct'}, {'domain': '.qq.com',
                                                                               'expiry': 1617555625, 'httpOnly': False,
                                                                               'name': 'Qs_pv_323937', 'path': '/',
                                                                               'secure': False,
                                                                               'value': '4166515209614860300'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.logined', 'path': '/',
                'secure': False, 'value': 'true'}, {'domain': '.qq.com', 'expiry': 1899460317, 'httpOnly': False,
                                                    'name': 'XWINDEXGREY', 'path': '/', 'secure': False,
                                                    'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                                                                    'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                                                                    'value': 'qbvXlwEoyo2PsvnmV9IP0OR5AbooOSy3L5NEPop5WFjVOd0RVcnkG9g4R3DOyLEWMm2FBzy6KD4IBP_lcGFwn34gkBgNRuwSUHP_NbtV1p0zR_6qLlsHY5C7OgdRc28uMghNJ66oVDGjMigIliEcsH4HpdYePkhbHVWZmqB4IXT5G4KGlQ8a8PaBDeTKtwubcb0eSHAzengZMrexXStoBSkT4uFCZ_J15LujfV6qVQ18Sg6Di9VoiqUy4BPbDIFdR9ZzIbSKcN7h6WNI_jWNyw'}, {
                'domain': '.work.weixin.qq.com', 'expiry': 1621154519, 'httpOnly': False,
                'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                'value': '1589457782,1589617574,1589618432,1589618520'}, {'domain': '.qq.com',
                                                                          'expiry': 1895288402,
                                                                          'httpOnly': False, 'name': 'pac_uid',
                                                                          'path': '/', 'secure': False,
                                                                          'value': '1_1735339370'}, {
                'domain': '.qq.com', 'expiry': 1609640853, 'httpOnly': False,
                'name': 'LOLWebSet_AreaBindInfo_1735339370', 'path': '/', 'secure': False,
                'value': '%257B%2522areaid%2522%253A%25229%2522%252C%2522areaname%2522%253A%2522%25E5%25BC%2597%25E9%259B%25B7%25E5%25B0%2594%25E5%258D%2593%25E5%25BE%25B7%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221735339370%2522%252C%2522rolename%2522%253A%2522%25E8%25B4%25B0%25E5%2585%25ADSir%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1735339370%257C9%257C1735339370*%257C%257C%257C%257C%2525E8%2525B4%2525B0%2525E5%252585%2525ADSir*%257C%257C%257C1578104854%2522%252C%2522md5str%2522%253A%252225FDED79F7E81B551161DEAFD8DB45C9%2522%252C%2522roleareaid%2522%253A%25229%2522%252C%2522sPartition%2522%253A%25229%2522%257D'}, {
                'domain': '.qq.com', 'expiry': 1896402065, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
                'secure': False, 'value': '1cfbe41c3823d52c'}, {'domain': '.qq.com', 'expiry': 1619744450,
                                                                'httpOnly': False, 'name': 'uin_cookie', 'path': '/',
                                                                'secure': False, 'value': 'o1735339370'}, {
                'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
                'secure': False, 'value': '1735339370'}, {'domain': '.qq.com', 'expiry': 2147483646,
                                                          'httpOnly': False, 'name': 'ptcz', 'path': '/',
                                                          'secure': False,
                                                          'value': '712d73b4f6cf992c87a1325434b6d461594be8af12a69da691eedc68662d14e1'}, {
                'domain': '.qq.com', 'expiry': 1620989566, 'httpOnly': False, 'name': 'LW_sid', 'path': '/',
                'secure': False, 'value': 'q185r8o9m485B3X5N69697u8I6'}, {'domain': '.qq.com', 'expiry': 1591675842,
                                                                          'httpOnly': False, 'name': 'ptui_loginuin',
                                                                          'path': '/', 'secure': False,
                                                                          'value': '1141598581'}, {'domain': '.qq.com',
                                                                                                   'expiry': 1609385307,
                                                                                                   'httpOnly': False,
                                                                                                   'name': 'LW_uid',
                                                                                                   'path': '/',
                                                                                                   'secure': False,
                                                                                                   'value': 'k1l5D7N7I8D4F9P370G7g2v8l5'}, {
                'domain': '.qq.com', 'expiry': 2147483653, 'httpOnly': False, 'name': 'RK', 'path': '/',
                'secure': False, 'value': '+wIt14q4O2'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
                                                          'name': 'wxpay.corpid', 'path': '/', 'secure': False,
                                                          'value': '1970325077135414'}, {'domain': '.qq.com',
                                                                                         'expiry': 2147385600,
                                                                                         'httpOnly': False,
                                                                                         'name': 'pgv_pvi', 'path': '/',
                                                                                         'secure': False,
                                                                                         'value': '1948984320'}, {
                'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                'secure': False, 'value': '6098594250'}]
        
        print(self.driver.get_cookies())
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # self.driver.find_element_by_link_text("通讯录").click()
        # sleep(5)
        # db.close()
