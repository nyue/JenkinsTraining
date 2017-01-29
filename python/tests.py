# tests.py

import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import MyClass
import YourClass

class SimpleTest(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_pass(self):
        self.assertEqual(10, 7 + 3)

#    def test_fail(self):
#        self.assertEqual(11, 7 + 3)

class MyClassTest(unittest.TestCase):

    def test_creation(self):
        mc = MyClass.MyClass()
        self.assertEqual(mc.value,1)

class YourClassTest(unittest.TestCase):

    def test_creation(self):
        mc = YourClass.YourClass()
        self.assertEqual(mc.value,2)

    def test_getValue(self):
        mc = YourClass.YourClass()
        self.assertEqual(mc.getValue(),2)
