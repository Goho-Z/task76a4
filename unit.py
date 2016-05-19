# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_43c9a0e(1,2,3,4,5),7,'fail')
if __name__ == '__main__':
    unittest.main()