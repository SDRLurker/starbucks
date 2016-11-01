class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = x = 0
        right = n
        while left < right:
            x = (left+right) // 2
            if x * (x+1) // 2 <= n < (x+1)*(x+2) // 2:
                return x
            elif x * (x+1) // 2 > n:
                right = x - 1
            else:
                left = x+1
        a = x-1
        while True: 
            if a * (a+1) // 2 <= n < (a+1)*(a+2) // 2:
                break
            a += 1
        return a
        		

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
