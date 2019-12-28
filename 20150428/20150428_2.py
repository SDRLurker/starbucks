class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (dp[i-len(w)] or i - len(w) == -1):
                    dp[i] = True
        return dp[-1]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        wordDict = ["leet", "code"]
        self.assertEqual(s.wordBreak("leetcode", wordDict), True)
        wordDict = ["apple", "pen"]
        self.assertEqual(s.wordBreak("applepenapple", wordDict), True)
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertEqual(s.wordBreak("catsandog", wordDict), False)
        wordDict = ["car", "ca", "rs"]
        self.assertEqual(s.wordBreak("cars", wordDict), True)
        wordDict = ["aaaa", "aaa"]
        self.assertEqual(s.wordBreak("aaaaaaa", wordDict), True)
        ss = "dbacdbdacddabbaaaadababadad"
        wordDict = ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]
        self.assertEqual(s.wordBreak(ss, wordDict), True)

if __name__ == "__main__":
    unittest.main()
