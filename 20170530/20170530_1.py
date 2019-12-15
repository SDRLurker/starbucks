class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # #2 Single Pass [Accepted]
        y = m
        x = n
        for op in ops:
            y = min(y, op[0])
            x = min(x, op[1])
        return x*y
        
        # Approach #1 Brute Force [Time Limit Exceeded]
        ops_m = len(ops)
        arr = [[0 for _ in range(n)] for _ in range(m)]
        for op in ops:
            a, b = op
            for i in range(a):
                for j in range(b):
                    arr[i][j] += 1
        cnt = 0
        for row in arr:
            for x in row:
                if x == ops_m:
                    cnt +=1
        return cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.maxCount(3,3,[[2,2],[3,3]]), 4)

if __name__ == "__main__":
    unittest.main()
