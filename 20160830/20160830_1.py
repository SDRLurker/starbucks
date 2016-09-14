class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnts = [0 for x in range(26)]
        for c in s:
            cnts[ord(c)-ord('a')] += 1
        for i, c in enumerate(s):
            if cnts[ord(c)-ord('a')] == 1:
                return i
        return -1

def solve_string(solution, s, expected):
        return "%20s %8s %8s" % (s, expected, solution.firstUniqChar(s))

s = Solution()
print("%20s %8s %8s" % ("s", "Expected", "Result"))
print(solve_string(s, "leetcode", 0))
print(solve_string(s, "loveleetcode", 2))
