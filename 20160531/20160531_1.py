import sys
import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
	if num < 0:
		return False
	return int(math.log(num,2)) % 2 == 0 and 4 ** int(math.log(sys.maxint, 4)) % num == 0

s = Solution()
print "%10s %8s %8s" % ("Value", "Expected", "Result")
print "%10d %8s %8s" % (16, "True", str(s.isPowerOfFour(16)))
print "%10d %8s %8s" % (2, "False", str(s.isPowerOfFour(2)))
