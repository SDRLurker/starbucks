class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_cnt = {}
        for c in s:
            char_cnt[c] = char_cnt.get(c,0) + 1
        max_cnt = 0
        is_odd = 0
        for c in char_cnt:
            if char_cnt[c] % 2 == 0:
                max_cnt += char_cnt[c]
            else:
                is_odd = 1
                max_cnt += char_cnt[c] - 1
        return max_cnt + is_odd

def solve_string(solution, s, expected):
        return "%30s %8d %8d" % (s, expected, solution.longestPalindrome(s))

s = Solution()
print("%30s %8s %8s" % ("input", "Expected", "Result"))
print(solve_string(s, "abccccdd", 7))
