class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
	ws = s.split()
	return len(ws[-1]) if len(ws) > 0 else 0

s = Solution()
print "%20s %8s %8s" % ("Input", "Output", "Expected")
print "%20s %8d %8d" % ('""', s.lengthOfLastWord(""), 0)
print "%20s %8d %8d" % ('" "', s.lengthOfLastWord(" "), 0)
print "%20s %8d %8d" % ("Hello World", s.lengthOfLastWord("Hello World"), 5)
