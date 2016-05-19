# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_64b5cf(1,2,3),9,'fail')
if __name__ == '__main__':
    unittest.main()