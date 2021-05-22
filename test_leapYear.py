import unittest
import sys
from tmp import lpYear.py

class testCaseUnit(unittest.TestCase):
    def test_good(self):
        self.assertEqual(leapYear.leapYear(2020),True)
    def test_bad(self):
        self.assertEqual(wordc.wordcount(2021),False)
        

if __name__ == '__main__':
    unittest.main()
