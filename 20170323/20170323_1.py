class Solution(object):
    def insomnia(self, i):
        """
        :type i: int
        """
        n = 1
        chk = 0
        if i <= 0:
            return "insomnia"
        while n <= 100:
            ns = n * i
            digit = 0
            while ns > 0:
                digit |= 1 << (ns % 10)
                ns //= 10
            chk |= digit
            if chk >= 0x3ff:
                return str(n * i)
            n += 1
        return "insomnia"

def solve_string(solution, i, expected):
    return "%10d %10s %10s" % (i, expected, solution.insomnia(i))

s = Solution()
print("%10s %10s %10s" % ("i", "Expected", "Result"))
print(solve_string(s, 0, "insomnia"))
print(solve_string(s, 1, "10"))
print(solve_string(s, 2, "90"))
print(solve_string(s, 11, "110"))
print(solve_string(s, 1692, "5076"))
