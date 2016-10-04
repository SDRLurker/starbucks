class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ""
        cs = "0123456789abcdef"
        for _ in range(8):
            s = cs[num&0xf] + s
            num >>= 4
        s = s.lstrip("0")
        s = "0" if len(s) == 0 else s
        return s

def solve_string(s, num, expected):
        return "%10d %10s %10s" % (num, expected, s.toHex(num))

s = Solution()
print("%10s %10s %10s" % ("num", "Expected", "Result"))
print(solve_string(s, 26, "1a"))
print(solve_string(s, -1, "ffffffff"))
print(solve_string(s, 0, "0"))
