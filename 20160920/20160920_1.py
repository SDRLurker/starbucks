class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur_digit = 1
        s = 0
        while n > 0:
            p = 10 ** (cur_digit - 1)
            if n - (9 * cur_digit * p) > 0:
                n -= (9 * cur_digit * p)
                s += 9 * p
                cur_digit += 1
            else:
                break
        s += (n // cur_digit)
        if n % cur_digit > 0:
            s += 1
        digit_char = str(s)[n%cur_digit-1]
        return int(digit_char)

def solve_string(s, n, expected):
        return "%10d %10d %10d" % (n, expected, s.findNthDigit(n))

s = Solution()
print("%10s %10s %10s" % ("n", "Expected", "Result"))
print(solve_string(s, 3, 3))
print(solve_string(s, 11, 0))
