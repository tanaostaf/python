#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import truk


class TestMethods(unittest.TestCase): 

    def test_float(self):
        self.assertAlmostEqual(truk.suma_stor(5,6,2), 4.68, 2)
 
    def test_float_1(self):
        self.assertAlmostEqual(truk.suma_stor(8,10,5), 19.81, 2)
    
    @unittest.expectedFailure
    def test_float_2(self):
        self.assertAlmostEqual(truk.suma_stor(8,-10,5), 19.81, 2)


if __name__ == '__main__':
    unittest.main()

#python3 -m unittest -v lab_17.py


