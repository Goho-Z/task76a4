# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_ee8ee8(1,2,3,4,5,6,7,8,9,10),4,'fail')
if __name__ == '__main__':
    unittest.main()