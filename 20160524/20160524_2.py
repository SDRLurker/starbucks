#!/use/bin/python
# -*- coding:utf-8 -*-
class Solution(object):
    r = (lambda k:3**k, lambda k:(3**(k-1))*4, lambda k:(3**k)*2)
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        return self.r[n%3](n//3)

s = Solution()
t = int(raw_input())
for _ in range(t):
	n = int(raw_input())
	print s.integerBreak(n)