# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_17e46f6(1,2,3,4,5),4,'fail')
if __name__ == '__main__':
    unittest.main()