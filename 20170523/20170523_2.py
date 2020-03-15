class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_dic = {}
        for n in nums:
            cnt_dic[n] = cnt_dic.get(n, 0) + 1
        m_cnt = 0
        for n in cnt_dic:
            cnt = 0
            if cnt_dic.get(n+1, 0) > 0:
                cnt = cnt_dic[n] + cnt_dic.get(n+1, 0)            
            m_cnt = max(cnt, m_cnt)
        return m_cnt

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.findLHS([1,3,2,2,5,2,3,7]), 5)
        self.assertEqual(s.findLHS([1,1,1,1]), 0)

if __name__ == "__main__":
    unittest.main()
