# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_3e02e94(1,2),6,'fail')
if __name__ == '__main__':
    unittest.main()