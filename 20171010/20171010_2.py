class Solution:
    def numDecodings(self, s):
        for i in range(1, 9+1):
            ii = s.find("%02d" % i)
            if ii == 0 or (ii > 0 and s[ii-1] in '03456789') or s.startswith("0"):
                return 0
        #print(s)
        a = [0 for _ in range(len(s)+1)]
        for i in range(len(s)):
            #print(i, a)
            if s[i] != "0":
                a[i+1] = 1 if a[i] == 0 else a[i]
            if i > 0 and 11 <= int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) != 20:
                if i > 1 and 11 <= int(s[i-2:i]) <= 26:
                    a[i+1] = a[i] + a[i-1]
                else:
                    a[i+1] = a[i] * 2
            elif i > 0 and int(s[i-1:i+1]) in (10,20):
                a[i+1] = a[i-1] if a[i] > 1 else a[i]
            #print(i, a)
        return a[len(s)]


import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.numDecodings("12"), 2)
        self.assertEqual(s.numDecodings("226"), 3)
        self.assertEqual(s.numDecodings("0"), 0)
        self.assertEqual(s.numDecodings("01"), 0)
        self.assertEqual(s.numDecodings("012"), 0)
        self.assertEqual(s.numDecodings("10"), 1)
        self.assertEqual(s.numDecodings("110"), 1)
        self.assertEqual(s.numDecodings("1110"), 2)
        self.assertEqual(s.numDecodings("301"), 0)
        self.assertEqual(s.numDecodings("12120"), 3)
        self.assertEqual(s.numDecodings("04759"), 0)
        self.assertEqual(s.numDecodings("509"), 0)
        self.assertEqual(s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"), 589824)

if __name__ == "__main__":
    unittest.main()
