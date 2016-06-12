import math
import sys
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
	if n <= 0:
		return False
	return ( 3 ** int(math.log(sys.maxint)) ) % n == 0

s = Solution()
print "%10s %8s %8s" % ("Value", "Expected", "Result")
print "%10d %8s %8s" % (27, "True", str(s.isPowerOfThree(27)))
print "%10d %8s %8s" % (2, "False", str(s.isPowerOfThree(2)))
print "%10d %8s %8s" % (0, "False", str(s.isPowerOfThree(0)))
print "%10d %8s %8s" % (1, "True", str(s.isPowerOfThree(1)))
