class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([w[::-1] for w in s.split()])

def solve_string(solution, s, expected):
    return "%26s %26s %26s" % (s, expected, solution.reverseWords(s))

s = Solution()
print("%26s %26s %26s" % ("s", "Expected", "Result"))
print(solve_string(s, "Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"))
