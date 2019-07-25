class Solution:
    def is_prime(self, n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    def countPrimeSetBits(self, L: int, R: int) -> int:
        cnt = 0
        for i in range(L, R+1):
            if self.is_prime(bin(i).count("1")):
                cnt += 1
        return cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.countPrimeSetBits(6,10), 4)
        self.assertEqual(s.countPrimeSetBits(10,15), 5)
        self.assertEqual(s.countPrimeSetBits(842,888), 23)

if __name__ == "__main__":
    unittest.main()

