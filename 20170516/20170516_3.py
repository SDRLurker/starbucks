class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        c_set = set(candies)
        return min(len(set(c_set)), len(candies)//2)

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.distributeCandies([1,1,2,2,3,3]), 3)
        self.assertEqual(s.distributeCandies([1,1,2,3]), 2)
        self.assertEqual(s.distributeCandies([1,1,1,1,2,2,2,3,3,3]), 3)

if __name__ == "__main__":
    unittest.main()
