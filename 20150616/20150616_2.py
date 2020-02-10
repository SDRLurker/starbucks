class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = 0
        if len(matrix) == 0:
            return m
        cols = len(matrix[0])
        dp = [ [0 for x in range(cols+1) ] for y in range(len(matrix)+1) ]
        #print(dp)
        for y in range(1, len(matrix)+1):
            for x in range(1, cols+1):
                if matrix[y-1][x-1] == '1':
                    dp[y][x] = min(dp[y][x-1], dp[y-1][x-1], dp[y-1][x]) + 1
                    m = max(m, dp[y][x])
        return m * m


import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.maximalSquare([]), 0)
        i = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        self.assertEqual(s.maximalSquare(i), 4)
        i = [["1"]]
        self.assertEqual(s.maximalSquare(i), 1)
        i = [["0","0","0","0","0"],["1","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]
        self.assertEqual(s.maximalSquare(i), 1)

if __name__ == "__main__":
    unittest.main()
