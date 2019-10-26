class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        si = 0
        arr = []
        if not nums:
            return arr
        for i in range(len(nums)-1):
            if nums[i]+1 < nums[i+1]:
                arr.append(str(nums[si]) if si == i else "%d->%d" % (nums[si],nums[i]))
                si = i+1
        i = len(nums)-1
        arr.append(str(nums[si]) if si == i else "%d->%d" % (nums[si],nums[i]))
        return arr

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.summaryRanges([0,1,2,4,5,7]), ["0->2","4->5","7"])
        self.assertEqual(s.summaryRanges([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])
        self.assertEqual(s.summaryRanges([]), [])

if __name__ == "__main__":
    unittest.main()
