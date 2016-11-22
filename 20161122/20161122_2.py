class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        n = len(str)
        if str[0] * n == str:
            return True
        d = 2
        while d*d <= n:
            if n % d == 0:
                divs = (d, n//d)
                for div in divs:
                    diff = False
                    for i in range(1, n//div):
                        if str[:n//div] != str[i*(n//div):(i+1)*(n//div)]:
                            diff = True
                            break
                    if not diff:
                        return True
            d += 1
        return False

def solve_string(s, str, expected):
    return "%20s %10s %10s" % (str, expected, s.repeatedSubstringPattern(str))

s = Solution()
print("%20s %10s %10s" % ("str", "Expected", "Result"))
print(solve_string(s, "a", False))
