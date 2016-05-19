# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_2ec2e14(1,2,3,4),8,'fail')
if __name__ == '__main__':
    unittest.main()