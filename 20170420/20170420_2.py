class Solution(object):
    def power_digit_sum(self, n):
        """
        :type n: int
        :rtype: int
        """
        pn = 2 ** n
        s = 0
        while pn > 0:
            s += pn % 10
            pn //= 10
        return s

def solve_string(s, n, expected):
    return "%10d %10d %10d" % (n, expected, s.power_digit_sum(n))

s = Solution()
print("%10s %10s %10s" % ("n", "Expected", "Result"))
print(solve_string(s, 3, 8))
print(solve_string(s, 4, 7))
print(solve_string(s, 7, 11))
