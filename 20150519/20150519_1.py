from typing import List

class Solution(object):
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt_dic = {}
        for i in range(len(s)-10+1):
            t = s[i:i+10]
            cnt_dic[t] = cnt_dic.get(t, 0) + 1
        return [k for k in cnt_dic if cnt_dic[k] > 1]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        i = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        o = ["AAAAACCCCC", "CCCCCAAAAA"]
        self.assertEqual(s.findRepeatedDnaSequences(i), o)
        i = "AAAAAAAAAAA"
        o = ["AAAAAAAAAA"]
        self.assertEqual(s.findRepeatedDnaSequences(i), o)

if __name__ == "__main__":
    unittest.main()
