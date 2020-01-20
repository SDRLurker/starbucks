﻿#!/usr/bin/python
# -*- coding: utf-8 -*-
# Complete the caesarCipher function below.
import math
def encryption(s):
    l = int(math.ceil(len(s)**0.5))
    return " ".join([s[i::l] for i in range(l)])

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(encryption("haveaniceday"), "hae and via ecy")
        self.assertEqual(encryption("feedthedog"), "fto ehg ee dd")
        self.assertEqual(encryption("chillout"), "clu hlt io")
        self.assertEqual(encryption("iffactsdontfittotheorychangethefacts"), "isieae fdtonf fotrga anoyec cttctt tfhhhs")

if __name__ == "__main__":
    unittest.main()
