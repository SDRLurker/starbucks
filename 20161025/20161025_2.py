class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        indice = []
        if not s or len(s) < len(p):
            return []
        p_cnt = [0 for x in range(26)]
        s_cnt = [0 for x in range(26)]
        for c in p:
            p_cnt[ord(c)-ord('a')] += 1
        for c in s[:len(p)]:
            s_cnt[ord(c)-ord('a')] += 1
        si = len(p)
        while si < len(s):
            if s_cnt == p_cnt:
                indice.append(si-len(p))
            s_cnt[ord(s[si-len(p)])-ord('a')] -= 1
            s_cnt[ord(s[si])-ord('a')] += 1
            si += 1
        if s_cnt == p_cnt:
            indice.append(si-len(p))
        return indice

def solve_string(solution, s, p, expected):
	return "%10s %10s %20s %20s" % (s, p, expected, solution.findAnagrams(s,p))

s = Solution()
print("%10s %10s %20s %20s" % ("s", "p", "Expected", "Result"))
print(solve_string(s, "cbaebabacd", "abc", [0,6]))
print(solve_string(s, "abab", "ab", [0,1,2]))
