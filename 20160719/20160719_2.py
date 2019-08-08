class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        nums = [[i,j] for i in nums1 for j in nums2]
        nums.sort(key=lambda x:x[0]+x[1])
        if len(nums) < k:
            return nums
        else:
            return nums[:k]
        
import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.kSmallestPairs([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]])
        self.assertEqual(s.kSmallestPairs([1,1,2], [1,2,3], 2), [[1,1],[1,1]])
        self.assertEqual(s.kSmallestPairs([1,2], [3], 3), [[1,3],[2,3]])

if __name__ == "__main__":
    unittest.main()
