#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


class BaseApi():
    def send(self,**data):
        return requests.request(**data).json()