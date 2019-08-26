class Solution(object):
    def countLetter(self, s):
        cnt_dic = {}
        for c in s:
            cnt_dic[c] = cnt_dic.get(c, 0) + 1
        return cnt_dic

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        answer = []
        p_dic = self.countLetter(p)
        s_dic = self.countLetter(s[:len(p)])
        for i in range(len(s)-len(p)):
            if p_dic == s_dic:
                answer.append(i)
            if i + len(p) < len(s):
                s_dic[s[i+len(p)]] = s_dic.get(s[i+len(p)], 0) + 1
            if s[i] in s_dic:
                s_dic[s[i]] = s_dic[s[i]] - 1
                if s_dic[s[i]] == 0:
                    s_dic.pop(s[i])


        if p_dic == s_dic:
            answer.append(i+1)
        return answer

def solve_string(solution, s, p, expected):
	return "%10s %10s %20s %20s" % (s, p, expected, solution.findAnagrams(s,p))

s = Solution()
print("%10s %10s %20s %20s" % ("s", "p", "Expected", "Result"))
print(solve_string(s, "cbaebabacd", "abc", [0,6]))
print(solve_string(s, "abab", "ab", [0,1,2]))
