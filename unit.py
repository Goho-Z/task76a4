# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_103b13e(1,2,3,4),7,'fail')
if __name__ == '__main__':
    unittest.main()