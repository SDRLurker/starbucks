class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        answer = [0 for x in range(max(l1, l2) + 1)]
        for i in range(len(answer)-1):
            d1 = ord(num1[l1-1-i]) - ord('0') if i < len(num1) else 0
            d2 = ord(num2[l2-1-i]) - ord('0') if i < len(num2) else 0
            answer[i] += (d1+d2)
            answer[i+1] += answer[i] // 10
            answer[i] %= 10
        result = "".join([str(c) for c in answer[::-1]]).lstrip("0")
        return "0" if len(result) == 0 else result

def solve_string(s, n1, n2, expected):
	return "%10s %10s %20s %20s" % (n1, n2, expected, s.addStrings(n1,n2))

s = Solution()
print("%10s %10s %20s %20s" % ("num1", "num2", "Expected", "Result"))
print(solve_string(s, "0", "0", "0"))
print(solve_string(s, "584", "18", "602"))
