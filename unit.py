# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_13611f1(1,2,3),0,'fail')
if __name__ == '__main__':
    unittest.main()