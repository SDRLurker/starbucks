import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmpx = x
        while tmpx > 0:
            if int(math.log10(x)) == 0:
                return True
            tmpx -= 10 ** int(math.log10(tmpx)) * (tmpx % 10)
            if tmpx < 0 or int(math.log10(x)) == int(math.log10(tmpx)):
                return False
            tmpx -= (tmpx % 10)
            tmpx //= 10
            x = tmpx
        return True

def solve_string(s, x, expected):
	return "%15d %10s %10s" % (x, expected, s.isPalindrome(x))

s = Solution()
print "%15s %10s %10s" % ("input", "Expected", "Result")
print solve_string(s, -21, False)
print solve_string(s, 0, True)
print solve_string(s, 121, True)
print solve_string(s, 1000021, False)
