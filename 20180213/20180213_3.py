class Solution(object):
    def kthGrammar(self, N, K, inv_cnt = 0):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return inv_cnt % 2
        if K % 2 == 0:
            v = self.kthGrammar(N-1, K//2, inv_cnt + 1)
        else:
            v = self.kthGrammar(N-1, (K+1)//2, inv_cnt)
        return v

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.kthGrammar(1, 1), 0)
        self.assertEqual(s.kthGrammar(2, 1), 0)
        self.assertEqual(s.kthGrammar(2, 2), 1)
        self.assertEqual(s.kthGrammar(4, 5), 1)
        self.assertEqual(s.kthGrammar(30, 434991989), 0)
        self.assertEqual(s.kthGrammar(4, 7), 0)
        self.assertEqual(s.kthGrammar(3, 2), 1)

if __name__ == "__main__":
    unittest.main()
