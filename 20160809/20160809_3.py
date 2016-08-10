import math
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n2_len = len(num2)
        n1_len = len(num1)
        result = [0 for x in xrange(n1_len+n2_len)]
        
        for i2, c2 in enumerate(num2[::-1]):
            i = i2
            for i1, c1 in enumerate(num1[::-1]):
                result[i] += int(c2) * int(c1)
                i += 1
            for i in xrange(len(result) - 1):
                result[i+1] += (result[i] // 10)
                result[i] = result[i] % 10
        
        result = "".join([str(c) for c in result[::-1]]).lstrip("0")
        return result if result != "" else "0"

def solve_string(s, n1, n2, expected):
	return "%10s %10s %20s %20s" % (n1, n2, expected, s.multiply(n1,n2))

s = Solution()
print "%10s %10s %20s %20s" % ("num1", "num2", "Expected", "Result")
print solve_string(s, "0", "0", "0")
print solve_string(s, "123123123", "0", "0")
print solve_string(s, "123123123", "123123123", "15159303417273129")
