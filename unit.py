# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_3c4dd6c(1,2,3,4,5),2,'fail')
if __name__ == '__main__':
    unittest.main()