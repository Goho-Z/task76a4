# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_3b222e9(1,2,3,4),9,'fail')
if __name__ == '__main__':
    unittest.main()