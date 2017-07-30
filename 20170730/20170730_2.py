class Solution:
    def factor(self, n):
        if n <= 0:
            return {}
        f = {}
        for k in [2,3,5,7,11,13,17,19,23,29,31,37,41]:
                while not (n % k):
                    f[k] = f.setdefault(k, 0) + 1
                    n //= k
        while n != 1:
            if k > n**0.5:
                f[n] = 1
                break
            while not (n%k):
                f[k] = f.setdefault(k, 0) + 1
                n //= k
            k += 2
        return f
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        fs = self.factor(n)
        m = 0
        for f in fs:
            m += f * fs[f]
        return m 

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.minSteps(2),2)
        self.assertEqual(s.minSteps(3),3)
        self.assertEqual(s.minSteps(4),4)
        self.assertEqual(s.minSteps(5),5)
        self.assertEqual(s.minSteps(6),5)
        self.assertEqual(s.minSteps(7),7)
        self.assertEqual(s.minSteps(8),6)
        self.assertEqual(s.minSteps(10),7)
        self.assertEqual(s.minSteps(11),11)
        self.assertEqual(s.minSteps(12),7)

if __name__ == "__main__":
    unittest.main()
