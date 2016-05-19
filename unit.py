# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_37c2434(1),4,'fail')
if __name__ == '__main__':
    unittest.main()