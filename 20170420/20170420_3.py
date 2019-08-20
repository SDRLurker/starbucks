class Solution:
    def optimalDivision(self, nums):
        if len(nums) == 0:
            return ""
        elif len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return "%d/%d" % (nums[0], nums[1])
        return "%d/(%s)" % (nums[0], "/".join([str(n) for n in nums[1:]]))
        
import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.optimalDivision([1000,100,10,2]), "1000/(100/10/2)")
        self.assertEqual(s.optimalDivision([3,2]), "3/2")

if __name__ == "__main__":
    unittest.main()

