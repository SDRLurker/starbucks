import math
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        s = n / 10 + (n % 10 != 0)
        for i in range(1,int(math.log10(n))+1):
            s += (n // (10**(i+1)))*(10**i) + min(max(n%(10**(i+1))-(10**i)+1, 0), (10**i))
        return s
        
import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.countDigitOne(13), 6)
        self.assertEqual(s.countDigitOne(-1), 0)

if __name__ == "__main__":
    unittest.main()
