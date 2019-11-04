from typing import List

class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        ti = 0
        for i, n in enumerate(nums):
            ti = i
            if target <= n:                
                break
        if target > nums[-1]:
            ti = len(nums)
        return ti

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.searchInsert([1,3,5,6], 5), 2)
        self.assertEqual(s.searchInsert([1,3,5,6], 2), 1)
        self.assertEqual(s.searchInsert([1,3,5,6], 7), 4)
        self.assertEqual(s.searchInsert([1,3,5,6], 0), 0)
        self.assertEqual(s.searchInsert([1,3,5,6], 6), 3)

if __name__ == "__main__":
    unittest.main()
