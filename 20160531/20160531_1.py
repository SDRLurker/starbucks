import sys
import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
	return num & (num-1) == 0 and num & 0x55555555 > 0

s = Solution()
print "%10s %8s %8s" % ("Value", "Expected", "Result")
print "%10d %8s %8s" % (16, "True", str(s.isPowerOfFour(16)))
print "%10d %8s %8s" % (2, "False", str(s.isPowerOfFour(2)))
print "%10d %8s %8s" % (0, "False", str(s.isPowerOfFour(0)))
print "%10d %8s %8s" % (1, "True", str(s.isPowerOfFour(1)))
