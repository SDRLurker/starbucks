class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for ri in range(numRows):
            row = [ 1 if i in (0, ri) else res[ri-1][i-1] + res[ri-1][i] for i in range(ri+1)]
            res.append(row)
        return res

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        o = [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]
        self.assertEqual(s.generate(5), o)

if __name__ == "__main__":
    unittest.main()
