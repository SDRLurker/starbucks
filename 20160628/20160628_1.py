class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left = 1
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                return True
        return False

s = Solution()
print "%5s %10s %10s" % ("input", "Expected", "Result")
print "%5d %10s %10s" % (16, "True", s.isPerfectSquare(16))
print "%5s %10s %10s" % ("input", "Expected", "Result")
print "%5d %10s %10s" % (14, "False", s.isPerfectSquare(14))
