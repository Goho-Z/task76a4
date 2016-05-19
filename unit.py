# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_3d0c7f7(1,2),4,'fail')
if __name__ == '__main__':
    unittest.main()