class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        t = ''
        while n > 0:
            t = chr(n%26 + ord('A')-1) + t
            n //= 26
        return t

def solve_string(s, n, expected):
    return "%10d %10s %10s" % (n, expected, s.convertToTitle(n))

s = Solution()
print("%10s %10s %10s" % ("n", "Expected", "Result"))
print(solve_string(s, 1, "A"))
print(solve_string(s, 26, "Z"))
print(solve_string(s, 27, "AA"))
print(solve_string(s, 28, "AB"))
