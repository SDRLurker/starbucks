class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i <<= 1
        return num ^ (i-1)

def solve_string(s, num, expected):
    return "%15d %15d %15d" % (num, expected, s.findComplement(num))

s = Solution()
print("%15s %15s %15s" % ("nums", "Expected", "Result"))
print(solve_string(s, 5, 2))
print(solve_string(s, 1, 0))
print(solve_string(s, 8, 7))
