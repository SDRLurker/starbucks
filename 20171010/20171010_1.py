class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        arow = [sum(grid[0][:i+1]) for i in range(len(grid[0]))]
        #if len(grid) == 1:
        #    return arow[-1]
        for y in range(1, len(grid)):
            brow = [0 for _ in range(len(grid[y]))]
            for x, v in enumerate(grid[y]):
                if x == 0:
                    brow[x] += (arow[x] + v)
                else:
                    brow[x] += (min(arow[x], brow[x-1]) + v)
            arow = brow
        return arow[-1]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.minPathSum([[0]]),0)
        self.assertEqual(s.minPathSum([[1,2,3,4],[4,3,2,1]]),9)
        self.assertEqual(s.minPathSum([[0,0],[0,0]]),0)

if __name__ == "__main__":
    unittest.main()
