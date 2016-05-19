# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_1cc5208(1,2,3),9,'fail')
if __name__ == '__main__':
    unittest.main()