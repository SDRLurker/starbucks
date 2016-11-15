class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        
        while l < r:
            while not s[l].isalnum():
                l += 1
            while not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

def solve_string(solution, s, expected):
    return "%40s %10s %10s" % (s, expected, solution.isPalindrome(s))

s = Solution()
print("%40s %10s %10s" % ("nums", "Expected", "Result"))
print(solve_string(s, "A man, a plan, a canal: Panama", True))
print(solve_string(s, "race a car", False))
print(solve_string(s, ".,", True))
