import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        digit = int(math.log10(x))
        while x > 0:
            x -= 10 ** digit * (x % 10)
            if x == 0:
                break
            if x < 0 or int(math.log10(x)) == digit:
                return False
            x -= (x % 10)
            x //= 10
            digit -= 2
        return True

def solve_string(s, x, expected):
	return "%15d %10s %10s" % (x, expected, s.isPalindrome(x))

s = Solution()
print "%15s %10s %10s" % ("input", "Expected", "Result")
print solve_string(s, -21, False)
print solve_string(s, 0, True)
print solve_string(s, 121, True)
print solve_string(s, 1000021, False)
