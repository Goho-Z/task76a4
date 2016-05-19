# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_57e6ef4(1,2,3,4,5,6,7,8,9),8,'fail')
if __name__ == '__main__':
    unittest.main()