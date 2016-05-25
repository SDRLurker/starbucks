#!/use/bin/python
# -*- coding:utf-8 -*-
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        ff = sorted(freq.items(), key=lambda f:f[1])
        return [x[0] for x in ff[-k:]]

s = Solution()
print s.topKFrequent([1,1,1,2,2,3],2)