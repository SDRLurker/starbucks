#!/use/bin/python
# -*- coding:utf-8 -*-
class Solution(object):
    def isVowel(self, c):
        vowels = list('aeiouAEIOU')
        return c in vowels

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_l = list(s) 
	s_idx = 0
	e_idx = len(s)-1
	while s_idx <= e_idx:
	    while s_idx < len(s)-1 and self.isVowel(str_l[s_idx]) == False:
	        s_idx += 1
	    while e_idx > 0 and self.isVowel(str_l[e_idx]) == False:
	        e_idx -= 1
	    if s_idx > e_idx:
	    	break
            str_l[s_idx], str_l[e_idx] = str_l[e_idx], str_l[s_idx]
	    s_idx += 1
	    e_idx -= 1

        return "".join(str_l)

s = Solution()
t = int(raw_input())
for _ in range(t):
	src_str = raw_input()
	print s.reverseVowels(src_str)
