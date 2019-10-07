class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        bef_row = []
        for y, row in enumerate(obstacleGrid):
            cur_row = [0 for v in row]
            for x, col in enumerate(row):
                if bef_row:
                    if x == 0:
                        cur_row[x] = bef_row[x] if col == 0 else 0
                    else:
                        cur_row[x] = (bef_row[x] + cur_row[x-1]) if col == 0 else 0
                else:
                    if x == 0:
                        cur_row[x] = 1 if col == 0 else 0
                    else:  
                        cur_row[x] = 1 if col == 0 and cur_row[x-1] else 0
            bef_row = cur_row
        return cur_row[-1]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        i = [[0,0,0], [0,1,0], [0,0,0]]
        self.assertEqual(s.uniquePathsWithObstacles(i), 2)
        i = [[0,0,0], [0,0,0], [0,0,0]]
        self.assertEqual(s.uniquePathsWithObstacles(i), 6)
        i = [[1,0]]
        self.assertEqual(s.uniquePathsWithObstacles(i), 0)
        i = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.assertEqual(s.uniquePathsWithObstacles(i), 0)

if __name__ == "__main__":
    unittest.main()
