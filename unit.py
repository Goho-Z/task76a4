# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_4a1f78a(1),7,'fail')
if __name__ == '__main__':
    unittest.main()