class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
            if l > r:
                break
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

def solve_string(solution, s, expected):
    return "%40s %10s %10s" % (s, expected, solution.isPalindrome(s))

s = Solution()
print("%40s %10s %10s" % ("s", "Expected", "Result"))
print(solve_string(s, "A man, a plan, a canal: Panama", True))
print(solve_string(s, "race a car", False))
print(solve_string(s, ".,", True))
