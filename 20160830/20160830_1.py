class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnts = [[0,0] for x in range(26)]
        idx = -1
        for i, c in enumerate(s):
            cnts[ord(c)-ord('a')][0] = i
            cnts[ord(c)-ord('a')][1] += 1
        minidx = len(s)
        for item in cnts:
            if item[1] == 1 and minidx > item[0]:
                minidx = item[0]
        if minidx < len(s):
            idx = minidx
        return idx

def solve_string(solution, s, expected):
        return "%20s %8s %8s" % (s, expected, solution.firstUniqChar(s))

s = Solution()
print("%20s %8s %8s" % ("s", "Expected", "Result"))
print(solve_string(s, "leetcode", 0))
print(solve_string(s, "loveleetcode", 2))
