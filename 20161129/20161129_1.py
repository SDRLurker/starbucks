class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for d in (2, 3, 5):
            while num % d == 0:
                num = num // d
        return num == 1

def solve_string(s, num, expected):
    return "%12d %10s %10s" % (num, expected, s.isUgly(num))

s = Solution()
print("%12s %10s %10s" % ("num", "Expected", "Result"))
print(solve_string(s, -2147483648, False))
print(solve_string(s, 6, True))
print(solve_string(s, 8, True))
print(solve_string(s, 48, True))
print(solve_string(s, 14, False))
