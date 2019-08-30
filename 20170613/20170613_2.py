import itertools
class Solution:
    def triangleNumber(self, nums):
        cnt = 0
        tris = itertools.combinations(nums, 3)
        for tri in tris:
            a, b, c = tri[0], tri[1], tri[2]
            if a + b > c and a + c > b and b + c > a:
                cnt += 1
        return cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.triangleNumber([2,2,3,4]), 3)
        self.assertEqual(s.triangleNumber([17,52,16,54,80,86,93,56,20,7,34,99,23,89,88,37,53,81,18,44,69,83,50,65,25,94,92,86,71,91,98,58,65,95,94,69,99,85,83,27,32,18,71,7,37,23,79,11,14,39,80,25,50,20,50,61,86,42,63,37,3,14,13,70,12,57,53,11,63,63,100,38,5,25,69,75,88,23,36,29,92,53,58,92,25,54,32,86,76,87,76,50,54,67,40,47,3,92,36,73]), 90315)
        self.assertEqual(s.triangleNumber([49,82,0,69,33,82,56,93,60,87,20,49,62,76,5,62,89,14,14,38,19,0,77,21,99,85,74,7,34,13,13,73,22,75,23,36,87,60,74,59,70,52,45,80,96,53,65,28,54,41,61,26,25,40,84,14,89,24,19,42,8,5,70,42,15,49,73,88,100,92,6,5,86,17,26,99,64,28,31,88,100,97,47,81,42,59,55,18,80,43,48,100,43,29,14,90,8,6,38,84]), 76307)
        self.assertEqual(s.triangleNumber([77,100,9,64,59,39,76,73,48,30,33,49,30,60,30,33,40,15,14,78,43,85,37,8,89,69,24,21,64,33,72,29,96,2,34,12,100,48,33,83,92,53,60,10,95,42,79,23,22,12,77,5,30,46,23,45,74,77,15,5,91,33,57,26,90,70,77,11,26,98,35,80,51,10,56,89,86,3,80,52,69,100,46,80,22,56,46,2,7,38,58,10,16,81,42,82,57,25,35,82]), 77414)

if __name__ == "__main__":
    unittest.main()