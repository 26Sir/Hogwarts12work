#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWait:
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://home.testing-studio.com/')
    def test_wait1(self):
        self.driver.find_element(By.XPATH,'//*')
        sleep(3)
        