class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        minus = False
        if num < 0:
            minus = True
            num *= -1
        counts = [ 0 for i in range(20) ]
        sevens = [ 7 ** i for i in range(20) ]
        while num > 0:
            i = 0
            while sevens[i] <= num:
                i += 1
            i -= 1
            counts[i] += 1
            num -= sevens[i]
        result = ""
        if minus:
            result += "-"
        i = 19
        while counts[i] == 0:
            i -= 1
        while i >= 0:
            result += str(counts[i])
            i -= 1
        return result

def solve_string(s, num, expected):
    return "%10d %15s %15s" % (num, expected, s.convertToBase7(num))

s = Solution()
print("%10s %15s %15s" % ("nums", "Expected", "Result"))
print(solve_string(s, 100, "202"))
print(solve_string(s, -7, "-10"))
print(solve_string(s, 0, "0"))
