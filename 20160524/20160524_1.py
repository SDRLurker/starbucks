#!/use/bin/python
# -*- coding:utf-8 -*-
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_idx = {}
        for i,c in enumerate(s):
            if c in 'aeiouAEIOU':
                vowel_idx[i] = c
        r = ''
        back_idx = len(vowel_idx) - 1
        v_idx = sorted(vowel_idx.items())
        for i,c in enumerate(s):
            if c in 'aeiouAEIOU':
                r += str(v_idx[back_idx][1])
                back_idx -= 1
            else:
                r += c
        return r

s = Solution()
t = int(raw_input())
for _ in range(t):
	src_str = raw_input()
	print s.reverseVowels(src_str)