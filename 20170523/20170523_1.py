class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nr = len(nums)
        nc = len(nums[0]) if nr > 0 else 0        
        if nr*nc != r*c:
            return nums
        arr = [v for row in nums for v in row]
        o = [arr[y*c:y*c+c] for y in range(r)]
        return o

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        i = [[1,2],[3,4]]
        o = [[1,2,3,4]]
        self.assertEqual(s.matrixReshape(i, 1, 4), o)
        self.assertEqual(s.matrixReshape(i, 2, 4), i)
        i = [[1,2,3,4]]
        o = [[1,2],[3,4]]
        self.assertEqual(s.matrixReshape(i, 2, 2), o)
        i = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
        o = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
        self.assertEqual(s.matrixReshape(i, 4, 5), o)

if __name__ == "__main__":
    unittest.main()
