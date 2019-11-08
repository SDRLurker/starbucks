class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        s = 0
        a = nums[0]
        i = 0
        for _ in range(len(nums)):
            i = (i + k) % len(nums)
            b = nums[i]
            nums[i] = a
            a = b
            if s == i and i < len(nums) - 1:
                i += 1
                s = i
                a = nums[i]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        in_list = [1,2,3,4,5,6,7]
        out_list = [5,6,7,1,2,3,4]
        s.rotate(in_list,3)
        self.assertEqual(in_list, out_list)
        in_list = [-1,-100,3,99]
        out_list = [3,99,-1,-100]
        s.rotate(in_list,2)
        self.assertEqual(in_list, out_list)
        in_list = [1,2,3]
        out_list = [1,2,3]
        s.rotate(in_list,0)
        self.assertEqual(in_list, out_list)
        in_list = [1,2,3,4,5,6]
        out_list = [4,5,6,1,2,3]
        s.rotate(in_list,3)
        self.assertEqual(in_list, out_list)

if __name__ == "__main__":
    unittest.main()
