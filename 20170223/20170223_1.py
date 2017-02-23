class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.upper() == word or word.title() == word or word.lower() == word

def solve_string(s, word, expected):
    return "%20s %10s %10s" % (word, expected, s.detectCapitalUse(word))

s = Solution()
print("%20s %10s %10s" % ("word", "Expected", "Result"))
print(solve_string(s, "USA", True))
print(solve_string(s, "leetcode", True))
print(solve_string(s, "Google", True))
print(solve_string(s, "FlaG", False))
