#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyone.apiceshi.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
    
    def test_token(self):
        print(self.address.get_token())
    
    def test_adduser(self):
        print(self.address.adduser("six26" , "sange", "13899999999"))
    
    def test_getuser(self):
        print(self.address.getuser("six26"))
        
    def test_upadte(self):
        print((self.address.changeuser("six26" , "sangsse", "13899999999")))
    
    def test_delete(self):
        print(self.address.deleteuser("six26"))