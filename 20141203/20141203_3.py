class Solution:
    def restoreIpAddresses(self, s):
        self.ips = []
        a = [0 for _ in range(5)]
        self.backtrack(a, s, 0, 0)
        return self.ips
    
    def backtrack(self, a, s, k, p):
        if self.is_solution(a, s, k, p):
            self.ips.append(".".join(a[1:]))
        k = k + 1
        if k == 5:
            return
        c = self.candidate(a, s, k, p)
        for i in range(len(c)):
            a[k] = c[i]
            pp = p + len(c[i])
            self.backtrack(a, s, k, pp)

    def is_solution(self, a, s, k, p):
        return k == 4 and len(s) == p

    def candidate(self, a, s, k, p):
        c = []
        if p < len(s):
            c.append(s[p])
        if p+2 <= len(s) and int(s[p:p+2]) > 0 and s[p] != '0':
            c.append(s[p:p+2])
        if p+3 <= len(s) and 0 < int(s[p:p+3]) < 256 and s[p] != '0':
            c.append(s[p:p+3])
        return c

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        o = ["255.255.11.135","255.255.111.35"]
        self.assertEqual(s.restoreIpAddresses("25525511135"), o)
        o = ["1.2.3.4"]
        self.assertEqual(s.restoreIpAddresses("1234"), o)
        o = ["0.10.0.10","0.100.1.0"]
        self.assertEqual(s.restoreIpAddresses("010010"), o)

if __name__ == "__main__":
    unittest.main()
