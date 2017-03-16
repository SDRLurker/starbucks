class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        for i in range(0, len(s), 2*k):
            m = min(i+k, len(s))
            res += s[i:m][::-1]
            if i+k < len(s):
                m = min(i+2*k, len(s))
                res += s[i+k:m]
        return res


def solve_string(solution, s, k, expected):
    return "%20s %5d %20s %20s" % (s, k, expected, solution.reverseStr(s,k))

s = Solution()
print("%20s %5s %20s %20s" % ("s", "k", "Expected", "Result"))
print(solve_string(s, "abcdefg", 2, "bacdfeg"))
print(solve_string(s, "abcdef", 3, "cbadef"))
print(solve_string(s, "abcdefgh", 3, "cbadefhg"))
