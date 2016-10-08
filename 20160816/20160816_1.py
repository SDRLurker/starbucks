class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for c in ransomNote:
            idx = magazine.find(c)
            if idx < 0:
                return False
            magazine = magazine[:idx] + magazine[idx+1:]
        return True

def solve_string(s, r, m, expected):
	return "%10s %10s %10s %10s" % (r, m, expected, s.canConstruct(r,m))

s = Solution()
print("%10s %10s %10s %10s" % ("ransomNote", "magazine", "Expected", "Result"))
print(solve_string(s, "a", "b", False))
print(solve_string(s, "aa", "ab", False))
print(solve_string(s, "aa", "aab", True))
