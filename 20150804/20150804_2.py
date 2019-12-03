class Solution(object):
    def binary_search(self, arr, value):
        low = 0
        high = len(arr)-1
        while (low <= high):
            mid = (low+high)//2    
            if arr[mid] > value:
                high = mid - 1
            elif arr[mid] < value:
                low = mid + 1
            else:
                return mid 
        return -1    
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if len(row) > 0 and row[0] <= target <= row[-1]:
                i = self.binary_search(row, target)
                if i >= 0 and row[i] == target:
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

if __name__ == "__main__":
    unittest.main()
