# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_25712fb(1,2,3),10,'fail')
if __name__ == '__main__':
    unittest.main()