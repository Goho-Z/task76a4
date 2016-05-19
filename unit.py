# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_5934ded(1),3,'fail')
if __name__ == '__main__':
    unittest.main()