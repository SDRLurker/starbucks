class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            elif n & 0b11 == 0b11:
                if n == 3:
                    return s + 2
                n = n + 1
            elif n & 0x1 == 0x1:
                n = n - 1
            s = s + 1
        return s

def solve_string(s, n, expected):
        return "%10d %10d %10d" % (n, expected, s.integerReplacement(n))

s = Solution()
print("%10s %10s %10s" % ("n", "Expected", "Result"))
print(solve_string(s, 8, 3))
print(solve_string(s, 7, 4))
print(solve_string(s, 15, 5))
