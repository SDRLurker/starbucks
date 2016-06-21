class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for y in xrange(n):
            for x in xrange(y):
                tmp = matrix[y][x]
                matrix[y][x] = matrix[x][y]
                matrix[x][y] = tmp
        for y in xrange(n):
            for x in xrange(n//2):
                tmp = matrix[y][x]
                matrix[y][x] = matrix[y][n-x-1]
                matrix[y][n-x-1] = tmp

s = Solution()
print "%20s %20s %20s" % ("input", "Expected", "Result")
input = [[1,2],[3,4]]
result = [[1,2],[3,4]]
s.rotate(result)
print "%20s %20s %20s" % (str(input), "[[3,1],[4,2]]", str(result))
