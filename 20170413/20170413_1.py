class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        ss = []
        for c in s:
            if c != ' ':
                ss.append(c)
            else:
                result += ''.join(ss[::-1]) + ' '
                ss = []
        result += ''.join(ss[::-1])
        return result

def solve_string(solution, s, expected):
    return "%26s %26s %26s" % (s, expected, solution.reverseWords(s))

s = Solution()
print("%26s %26s %26s" % ("s", "Expected", "Result"))
print(solve_string(s, "Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"))
