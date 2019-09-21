class Solution:
    def findShortestSubArray(self, nums):
        cnt_dic = {}
        min_dic = {}
        max_dic = {}
        for i,num in enumerate(nums):
            cnt_dic[num] = cnt_dic.get(num, 0) + 1
            if num not in min_dic:
                min_dic[num] = i
                max_dic[num] = i
            else:
                max_dic[num] = i
        
        cnt_list = list(cnt_dic.items())
        cnt_list.sort(key=lambda kv:-kv[1])
        maxk, maxv = cnt_list[0]
        l = max_dic[maxk] - min_dic[maxk] + 1
        for k, v in cnt_list:
            if v == maxv:
                l = min(l, max_dic[k] - min_dic[k] + 1)
        return l

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.findShortestSubArray([1, 2, 2, 3, 1]), 2)
        self.assertEqual(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]), 6)

if __name__ == "__main__":
    unittest.main()
