import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self.backtrack(ans, [], candidates, target, 0)
        return ans
    
    def backtrack(self, ans, tmp_lst, candidates, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            t = copy.deepcopy(tmp_lst)
            if t not in ans:
                ans.append(t)
        else:
            for i, c in enumerate(candidates):
                if i >= start:
                    tmp_lst.append(c)
                    self.backtrack(ans, tmp_lst, candidates, remain - c, i+1)
                    tmp_lst.pop()

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        o = [[1,1,6],[1,2,5],[1,7],[2,6]]
        self.assertEqual(s.combinationSum2([10,1,2,7,6,1,5], 8), o)
        o = [[1,2,2],[5]]
        self.assertEqual(s.combinationSum2([2,5,2,1,2], 5), o)

if __name__ == "__main__":
    unittest.main()
