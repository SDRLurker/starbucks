import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        p = itertools.permutations(nums)
        p = list(set(p))
        p.sort()
        return p

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        o = [
                (1,2,3),
                (1,3,2),
                (2,1,3),
                (2,3,1),
                (3,1,2),
                (3,2,1)
        ]
        self.assertEqual(s.permute([1, 2, 3]), o)

if __name__ == "__main__":
    unittest.main()
