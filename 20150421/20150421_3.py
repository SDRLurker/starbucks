class Solution(object):
    def titleToNumber(self, s):
        a = 0
        for i, c in enumerate(s):
            a += ord(c) - ord('A') + 1
            if i < len(s) - 1:
                a *= 26
        return a

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.titleToNumber("A"), 1)
        self.assertEqual(s.titleToNumber("AB"), 28)
        self.assertEqual(s.titleToNumber("ZY"), 701)

if __name__ == "__main__":
    unittest.main()
