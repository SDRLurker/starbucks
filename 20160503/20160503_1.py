def del_num(w1, w2):
    total = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        total += abs(w1.count(letter) - w2.count(letter))
    return total

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(del_num("cde", "abc"), 4)

if __name__ == "__main__":
    unittest.main()
