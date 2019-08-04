class Solution:
    def dominantIndex(self, nums):
        m = -1
        mi = -1
        for i, n in enumerate(nums):
            if n > m:
                m = n
                mi = i
        nums.sort()
        if (len(nums) >= 2 and m >= 2*nums[-2]) or len(nums) == 1:
            return mi
        return -1
            
import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.dominantIndex([3, 6, 1, 0]), 1)
        self.assertEqual(s.dominantIndex([1, 2, 3, 4]), -1)
        self.assertEqual(s.dominantIndex([1]), 0)

if __name__ == "__main__":
    unittest.main()
