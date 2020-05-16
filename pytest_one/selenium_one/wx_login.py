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
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    
    def test_login(self):
        
        
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db=shelve.open("cookies")
        # db["cookie"]= self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_link_text("通讯录").click()
        sleep(5)
        db.close()
