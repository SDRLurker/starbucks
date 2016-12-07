class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ps_dic = {}
        sp_dic = {}
        strs = str.split()
        if len(pattern) != len(strs):
            return False
        for i,c in enumerate(pattern):
            if c not in ps_dic:
                ps_dic[c] = strs[i]
            if ps_dic[c] != strs[i]:
                return False
        for i,s in enumerate(strs):
            if s not in sp_dic:
                sp_dic[s] = pattern[i]
            if sp_dic[s] != pattern[i]:
                return False
        if len(ps_dic) != len(sp_dic):
            return False
        return True

def solve_string(s, pattern, str, expected):
    return "%10s %30s %10s %10s" % (pattern, str, expected, s.wordPattern(pattern, str))

s = Solution()
print("%10s %30s %10s %10s" % ("pattern", "str", "Expected", "Result"))
print(solve_string(s, "abba", "dog cat cat dog", True))
print(solve_string(s, "abba", "dog cat cat fish", False))
print(solve_string(s, "aaaa", "dog cat cat dog", False))
print(solve_string(s, "abba", "dog dog dog dog", False))