class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(s1)+len(s2) != len(s3):
            return False
        dp = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                        (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.isInterleave("aabcc","dbbca","aadbbcbcac"), True)
        self.assertEqual(s.isInterleave("aabcc","dbbca","aadbbbaccc"), False)
        self.assertEqual(s.isInterleave("","","a"), False)

if __name__ == "__main__":
    unittest.main()
