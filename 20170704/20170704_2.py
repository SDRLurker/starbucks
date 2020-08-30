class Solution(object):
    def smallestFactorization(self, a):
        if a < 2:
            return a
        res = 0 
        mul = 1
        for i in range(9, 2-1,-1):
            while a % i ==0:
                a /= i
                res = mul * i + res 
                mul *= 10
        return res

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.smallestFactorization(48), 68)
        self.assertEqual(s.smallestFactorization(15), 35)

if __name__ == "__main__":
    unittest.main()
