class Solution:
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "a"), "c")
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "c"), "f")
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "d"), "f")
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "g"), "j")
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "j"), "c")
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "k"), "c")
        self.assertEqual(s.nextGreatestLetter(["a", "b"], "z"), "a")

if __name__ == "__main__":
    unittest.main()
