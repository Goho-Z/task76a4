# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_40fe0a6(1),10,'fail')
if __name__ == '__main__':
    unittest.main()