class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        e = []
        s = []
        for n in nums:
            if n not in s:
                s.append(n)
            else:
                e.append(n)
        s = list( set(range(1,len(nums)+1)) - set(nums) )
        e.append(s[0])
        return e

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.findErrorNums([1,2,2,4]), [2,3])
        self.assertEqual(s.findErrorNums([3,2,2,4]), [2,1])

if __name__ == "__main__":
    unittest.main()
