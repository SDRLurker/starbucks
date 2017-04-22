class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        for c in s:
            if c == 'A':
                a += 1
                l = 0
            elif c == 'L':
                l += 1
            else:
                l = 0
            if a > 1 or l > 2:
                return False
        return True

def solve_string(solution, s, expected):
    return "%40s %10s %10s" % (s, expected, solution.checkRecord(s))

s = Solution()
print("%40s %10s %10s" % ("s", "Expected", "Result"))
print(solve_string(s, "PPALLP", True))
print(solve_string(s, "PPALLL", False))
print(solve_string(s, "ALLAPPL", False))
print(solve_string(s, "LLLL", False))
print(solve_string(s, "LALL", True))
print(solve_string(s, "LLPPLPPLPLPPLPLPLPPAPPPPPLPALL", False))
