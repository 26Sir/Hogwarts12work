#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from pytest_one.calc_one.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()
    
    @pytest.mark.parametrize('a,b,c',[(0,0,0),(-1,1,0),(-1,-3,-4),(0.5,0.5,1)])
    def test_add_1(self,a,b,c):
        result = self.calc.add(a,b)
        print(result)
        assert c == result

    def test_div(self):
        # self.calc = Calc()
        result_1 = self.calc.div(2,2)
        assert 1 == result_1
        
if __name__=='__main__':
    pytest.main(['-vs','test_pytest.py::TestCalc::test_div'])
