class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"
        output = ""
        for c in num:
            while len(output) > 0 and ord(output[-1]) > ord(c) and k > 0:
                output = output[:-1]
                k -=  1
            output += c
        if k > 0:
            output = output[:-k]
        output = output.lstrip("0")
        if len(output) == 0:
            output = "0"
        return output

def solve_string(s, num, k, expected):
        return "%10s %5d %10s %10s" % (num, k, expected, s.removeKdigits(num, k))

s = Solution()
print("%10s %5s %10s %10s" % ("num", "k", "Expected", "Result"))
print(solve_string(s, "1432219", 3, "1219"))
print(solve_string(s, "10200", 1, "200"))
print(solve_string(s, "10", 2, "0"))
print(solve_string(s, "9", 1, "0"))
print(solve_string(s, "1234567890", 9, "0"))
print(solve_string(s, "98765432101234567891234523456",15,"1231234523456"))
print(solve_string(s, "1111111",3,"1111"))
