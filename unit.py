# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_345a6bc(1,2,3,4),6,'fail')
if __name__ == '__main__':
    unittest.main()