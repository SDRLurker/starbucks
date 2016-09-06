class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        next_80 = 0
        while i < len(data):
            if next_80 == 0:
                if data[i] & 0x80 == 0:
                    next_80 = 0
                elif data[i] & 0xe0 == 0xc0:
                    next_80 = 1
                elif data[i] & 0xf0 == 0xe0:
                    next_80 = 2
                elif data[i] & 0xf8 == 0xf0:
                    next_80 = 3
                else:
                    return False
            else:
                if data[i] & 0xc0 == 0x80:
                    next_80 -= 1
                else:
                    return False
            i += 1
        return next_80 == 0

def solve_string(s, input, expected):
        return "%10s %10s %10s" % (input, expected, s.validUtf8(input))

s = Solution()
print("%10s %10s %10s" % ("input", "Expected", "Result"))
print(solve_string(s, [197,130,1], "True"))
print(solve_string(s, [235,140,4], "False"))
print(solve_string(s, [237], "False"))
