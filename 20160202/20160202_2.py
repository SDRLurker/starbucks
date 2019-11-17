class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.hammingWeight(0b00000000000000000000000000001011),3)
        self.assertEqual(s.hammingWeight(0b00000000000000000000000010000000),1)
        self.assertEqual(s.hammingWeight(0b11111111111111111111111111111101),31)

if __name__ == "__main__":
    unittest.main()
