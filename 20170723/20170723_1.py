class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = [0 for _ in range(len(nums)+1)]
        for n in nums:
            c[n] += 1
        a = b = 0
        for i in range(1,len(nums)+1):
            if c[i] == 0:
                b = i
            elif c[i] == 2:
                a = i
        return [a, b]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.findErrorNums([1,2,2,4]), [2,3])
        self.assertEqual(s.findErrorNums([3,2,2,4]), [2,1])

if __name__ == "__main__":
    unittest.main()
