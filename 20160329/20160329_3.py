#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the caesarCipher function below.
import math
def encryption(s):
    col = int(math.ceil(len(s)**0.5))
    arr = []
    for i in range(col):
        arr.append(s[i:len(s):col])
    return " ".join(arr)

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(encryption("haveaniceday"), "hae and via ecy")
        self.assertEqual(encryption("feedthedog"), "fto ehg ee dd")
        self.assertEqual(encryption("chillout"), "clu hlt io")

if __name__ == "__main__":
    unittest.main()

