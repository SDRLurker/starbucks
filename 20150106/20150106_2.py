class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        o = set()
        for i in range(2**len(nums)):
            s = [nums[ii] for ii in range(len(nums)) if i&(2**ii) == 2**ii]
            s.sort()
            o.add(tuple(s))
        o = list(o)
        o.sort()
        return o

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        expected = [(), (1,), (1, 2), (1, 2, 2), (2,), (2, 2)]
        self.assertEqual(s.subsetsWithDup([1,2,2]), expected)
        expected = [(), (1,), (1, 4), (1, 4, 4), (1, 4, 4, 4), (1,4,4,4,4),(4,),(4,4),(4,4,4),(4,4,4,4)]
        self.assertEqual(s.subsetsWithDup([4,4,4,1,4]), expected)

if __name__ == "__main__":
    unittest.main()
