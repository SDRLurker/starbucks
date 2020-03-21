class Solution:
    def __init__(self):
        self.abuns = set()
        for n in range(1, 10**5+1):
            a = self.is_abundant(n)
            if a:
                self.abuns.add(n)

    def is_abundant(self, n):
        if n < 12:
            return False
        #if n != 81081 and n % 2 == 1 and n % 5 != 0:
        #    return False
        s = set([1])
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                s.add(i)
                s.add(n // i)
        return sum(s) > n

    def is_two_abundant(self, n):
        if n > 20161:
            return True
        if n < 24:
            return False
        for i in range(12, n // 2 + 1):
            if not self.is_abundant(i):
                continue
            if self.is_abundant(n-i):
                return True
        return False

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.is_two_abundant(24), True)
        self.assertEqual(s.is_two_abundant(49), False)

if __name__ == "__main__":
    unittest.main()
    #s = Solution()
    #T = int(input())
    #for _ in range(T):
    #    N = int(input())
    #    print("YES" if s.is_two_abundunt(N) else "NO")
