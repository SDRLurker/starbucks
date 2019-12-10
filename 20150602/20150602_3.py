class Solution(object):
    def bsearch(self, arr, v):
        s = 0
        e = len(arr)
        while s < e:
            m = (s+e) // 2
            if arr[m] < v:
                s = m + 1
            elif arr[m] > v:
                e = m
            else:
                return m
        return -1
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]]:
            return False
        for row in matrix:
            if row[-1] < target:
                continue
            if self.bsearch(row, target) >= 0:
                return True
        return False
        
import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        arr = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        self.assertEqual(s.searchMatrix(arr, 5), True)
        self.assertEqual(s.searchMatrix(arr, 20), False)
        self.assertEqual(s.searchMatrix([[]], 1), False)
        arr = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
        self.assertEqual(s.searchMatrix(arr, 3), True)
        self.assertEqual(s.searchMatrix(arr, 13), False)

if __name__ == "__main__":
    unittest.main()
