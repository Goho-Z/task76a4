# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_2a42e57(1,2,3,4,5,6,7),7,'fail')
if __name__ == '__main__':
    unittest.main()