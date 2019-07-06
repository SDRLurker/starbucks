class Solution(object):
    def countBits(self, num):
        return [bin(i).count('1') for i in range(num+1)]

s = Solution()
print("%5s %20s %20s" % ("Value", "Expected", "Result"))
print("%5d %20s %20s" % (2, [0, 1, 1], str(s.countBits(2))))
print("%5d %20s %20s" % (5, [0, 1, 1, 2, 1, 2], str(s.countBits(5))))
