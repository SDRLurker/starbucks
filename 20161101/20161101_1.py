class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int( (-1+((1+8*n))**0.5) // 2) 
        		

def solve_string(s, n, expected):
    return "%10d %10d %10d" % (n, expected, s.arrangeCoins(n))

s = Solution()
print("%10s %10s %10s" % ("n", "Expected", "Result"))
print(solve_string(s, 0, 0))
print(solve_string(s, 5, 2))
print(solve_string(s, 8, 3))
print(solve_string(s, 10, 4))
print(solve_string(s, 100, 13))
print(solve_string(s, 1804289383, 60070))
