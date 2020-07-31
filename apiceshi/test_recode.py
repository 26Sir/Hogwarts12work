#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth


def test_demo():
    url = 'http://httpbin.testing-studio.com/cookies'
    header = {"Cookie": "sir=26Sir"}
    r = requests.get(url=url, headers=header)
    print(r.request.headers)


def test_oauth():
    r = requests.get(url='http://httpbin.testing-studio.com/basic-auth/26sir/123',
                     auth = HTTPBasicAuth("26sir","123"))
    print(r.text)
