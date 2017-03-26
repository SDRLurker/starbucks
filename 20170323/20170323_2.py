class Solution(object):
    def flip(self, s):
        stat = s[0]
        cnt = 0
        for i, c in enumerate(s):
            if stat != c:
                cnt += 1
                stat = c
        if s[-1] == '-':
            cnt += 1
        return cnt

def solve_string(solution, s, expected):
    return "%10s %10d %10d" % (s, expected, solution.flip(s))

s = Solution()
print("%10s %10s %10s" % ("s", "Expected", "Result"))
print(solve_string(s, "-", 1))
print(solve_string(s, "-+", 1))
print(solve_string(s, "+-", 2))
print(solve_string(s, "+++", 0))
print(solve_string(s, "--+-", 3))
