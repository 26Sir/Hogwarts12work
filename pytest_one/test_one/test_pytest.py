#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from pytest_one.calc_one.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result
    
    def test_div(self):
        # self.calc = Calc()
        result_1 = self.calc.div(2,2)
        assert 1 == result_1
        
if __name__=='__main__':
    pytest.main(['-vs','test_pytest.py::TestCalc::test_div'])
