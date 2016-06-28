class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1
        return False

s = Solution()
print "%5s %10s %10s" % ("input", "Expected", "Result")
print "%5d %10s %10s" % (16, "True", s.isPerfectSquare(16))
print "%5s %10s %10s" % ("input", "Expected", "Result")
print "%5d %10s %10s" % (14, "False", s.isPerfectSquare(14))
