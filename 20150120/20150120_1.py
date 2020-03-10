class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for y in range(1, len(triangle)):
            for x in range(len(triangle[y])):
                if x == 0:
                    triangle[y][x] += triangle[y-1][x]
                elif x == len(triangle[y]) - 1:
                    triangle[y][x] += triangle[y-1][-1]
                else:
                    triangle[y][x] += min(triangle[y-1][x-1], triangle[y-1][x])
        return min(triangle[-1])

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        i = [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
        self.assertEqual(s.minimumTotal(i), 11)

if __name__ == "__main__":
    unittest.main()
