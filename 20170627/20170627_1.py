# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-3]*nums[-2]*nums[-1], nums[-1]*nums[0]*nums[1])

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution() 
        self.assertEqual(s.maximumProduct([1,2,3]), 6)
        self.assertEqual(s.maximumProduct([1,2,3,4]), 24)
        self.assertEqual(s.maximumProduct([-4,-3,-2,-1,60]), 720)

if __name__ == "__main__":
    unittest.main()
