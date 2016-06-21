class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [ 0 for x in xrange(rowIndex+1) ]
        row[0] = 1
        for i in xrange(1, rowIndex+1):
            a = row[i-1]
            for j in xrange(1, i+1):
                b = row[j]
                row[j] = a+b
                a = b
        return row

s = Solution()
print "%10s %25s %25s" % ("input", "Expected", "Result")
input = 3
print "%10d %25s %25s" % (input, str([1,3,3,1]), str(s.getRow(3)))
input = 4
print "%10d %25s %25s" % (input, str([1,4,6,4,1]), str(s.getRow(4)))
