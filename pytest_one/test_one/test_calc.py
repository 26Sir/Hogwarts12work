#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')
import unittest
from pytest_one.calc_one.calc import Calc


class TestCalc(unittest.TestCase):
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        self.assertEqual(3, result)
# unittest.main()