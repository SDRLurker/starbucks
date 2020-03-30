class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        S = list(str(N))
        i = 1
        while i < len(S) and S[i-1] <= S[i]:
            i += 1
        while 0 < i < len(S) and S[i-1] > S[i]:
            S[i-1] = str(int(S[i-1]) - 1)
            i -= 1
        S[i+1:] = '9' * (len(S) - i - 1)
        return int("".join(S))

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.monotoneIncreasingDigits(10),9)
        self.assertEqual(s.monotoneIncreasingDigits(1234),1234)
        self.assertEqual(s.monotoneIncreasingDigits(332),299)
        self.assertEqual(s.monotoneIncreasingDigits(123454321),123449999)
        self.assertEqual(s.monotoneIncreasingDigits(333222),299999)

if __name__ == "__main__":
    unittest.main()
