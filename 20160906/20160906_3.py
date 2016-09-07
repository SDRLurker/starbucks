class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        cond_pairs = ((0x80,0),(0xe0,0xc0),(0xf0,0xe0),(0xf8,0xf0))
        next_80 = 0
        for byte in data:
            if next_80 == 0:
                next_80 = -1
                for idx, cond in enumerate(cond_pairs):
                    if byte & cond[0] == cond[1]:
                        next_80 = idx
                        break
                if next_80 < 0:
                    return False
            else:
                if byte & 0xc0 == 0x80:
                    next_80 -= 1
                else:
                    return False
        return next_80 == 0

def solve_string(s, input, expected):
        return "%10s %10s %10s" % (input, expected, s.validUtf8(input))

s = Solution()
print("%10s %10s %10s" % ("input", "Expected", "Result"))
print(solve_string(s, [197,130,1], "True"))
print(solve_string(s, [235,140,4], "False"))
print(solve_string(s, [237], "False"))
