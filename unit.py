# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_3ce500f(1),0,'fail')
if __name__ == '__main__':
    unittest.main()