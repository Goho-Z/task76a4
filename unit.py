# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_48b3846(1),5,'fail')
if __name__ == '__main__':
    unittest.main()