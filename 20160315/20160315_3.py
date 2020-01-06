#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the squares function below.
def timeInWords(h, m):
    hs = ["", "one", "two", "three", "four", "five",
        "six","seven","eight","nine","ten","eleven","twelve",
        "thirteen", "fourteen", "quarter", "sixteen",
        "seventeen", "eighteen", "nineteen", "twenty",
        "twenty one", "twenty two", "twenty three", 
        "twenty four", "twenty five", "twenty six",
        "twenty seven", "twenty eight", "twenty nine",
        "half"
        ]
    if m == 0:
        s = "%s o' clock" % hs[h]
    elif m >= 1 and m <= 30:
        ms = hs[m] 
        if m == 1:
            ms += " minute"
        elif m not in (15, 30):
            ms += " minutes"
            
        ms += " past"
        s = ms + " " + hs[h]
    elif m >= 31 and m < 60:
        ms = hs[60-m]
        if m not in (45,):
            ms += " minutes"
        ms += " to"
        s = ms + " " + hs[(h+1)%12]
    return s

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(timeInWords(5,0), "five o' clock")
        self.assertEqual(timeInWords(5,1), "one minute past five")
        self.assertEqual(timeInWords(5,10), "ten minutes past five")
        self.assertEqual(timeInWords(5,15), "quarter past five")
        self.assertEqual(timeInWords(5,30), "half past five")
        self.assertEqual(timeInWords(5,40), "twenty minutes to six")
        self.assertEqual(timeInWords(5,45), "quarter to six")
        self.assertEqual(timeInWords(5,47), "thirteen minutes to six")
        self.assertEqual(timeInWords(5,28), "twenty eight minutes past five")
        self.assertEqual(timeInWords(1,1), "one minute past one")

if __name__ == "__main__":
    unittest.main()

