class Solution(object):
    def check(self, matrix, s, w, h, x, y):
        while x < w and y < h:
            x += 1
            y += 1
            if x < w and y < h:
                if s != matrix[y][x]:
                    return False
        return True
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        h = len(matrix)
        w = len(matrix[0])
        for y in range(0, h-1):
            x = 0
            s = matrix[y][x]
            if not self.check(matrix, s, w, h, x, y):
                return False
        for x in range(1, w-1):
            y = 0
            s = matrix[y][x]
            if not self.check(matrix, s, w, h, x, y):
                return False
        return True

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.isToeplitzMatrix([[[1,2,3,4],[5,1,2,3],[9,5,1,2]]]), True)
        self.assertEqual(s.isToeplitzMatrix([[1,2],[2,2]]), False)

if __name__ == "__main__":
    unittest.main()
