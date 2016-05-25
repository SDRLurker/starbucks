#!/use/bin/python
# -*- coding:utf-8 -*-
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        r = 1
        while n > 4:
            n = n - 3
            r *= 3
        return r * n

s = Solution()
t = int(raw_input())
for _ in range(t):
	n = int(raw_input())
	print s.integerBreak(n)