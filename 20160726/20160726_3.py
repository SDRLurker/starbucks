class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lst = [str(i) for i in range(1,n+1)]
        lst.sort()
        lst2 = [int(i) for i in lst]
        return lst2

s = Solution()
print("%5s %35s %35s" % ("n", "Expected", "Result"))
print("%5d %35s %35s" % (13, str([1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]).replace(" ",""), str(s.lexicalOrder(13)).replace(" ","")))
