import unittest
from calc import Add

class Tests_Calc(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""),0)
        self.assertEqual(Add("1,2"),3)
    def test_more_numbers(self):
        self.assertEqual(Add("1,2,3,4"),10)  
    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            Add("1,n")         
    def test_newline(self):
        self.assertEqual(Add("1\n2,3"),6)
    def test_wrong_format(self):
        with self.assertRaises(ValueError):
            Add("1,\n")
