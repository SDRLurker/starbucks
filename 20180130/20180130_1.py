class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        cnt = 0
        for c in S:
            if c in J:
                cnt += 1
        return cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.numJewelsInStones("aA", "aAAbbbb"), 3)
        self.assertEqual(s.numJewelsInStones("z", "ZZ"), 0)

if __name__ == "__main__":
    unittest.main()
