class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 == 1:
            return False
        half = [False for _ in range(s//2+1)]
        half[0] = True
        ss = 0
        for num in nums:
            ss += num
            for i in range(ss,-1,-1):
                if num+i <= s//2 and half[i]:
                    half[num+i] = True
            if half[s//2]:
                return True
        return False

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.canPartition([1, 5, 5, 1]), True)
        self.assertEqual(s.canPartition([1, 2, 3, 5]), False)
        self.assertEqual(s.canPartition([1, 1, 1, 1]), True)
        self.assertEqual(s.canPartition([1, 2, 5]), False)

if __name__ == "__main__":
    unittest.main()
