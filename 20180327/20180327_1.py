class Solution:
    def customSortString(self, S: str, T: str) -> str:
        cnt_dic = {}
        s = ""
        for c in T:
            cnt_dic[c] = cnt_dic.get(c, 0) + 1
        for c in S:
            if c in T:
                s += c * cnt_dic[c]
                cnt_dic.pop(c)
        # 주석한 부분으로만 제출해도 OK
        #for c in cnt_dic:
        #    s += c * cnt_dic[c]
        # 정렬하지 말아야할 부분도 Testcase는 정렬해서 다음코드 추가.
        key = list(cnt_dic.keys())
        key.sort()
        for c in key:
            s += c * cnt_dic[c]
        return s

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.customSortString("cba","abcd"), "cbad")
        S = "hucw"
        T = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
        Expected = "hhhhhuucccwaaaaaaaaabbdddddeffffggggiijjjjkkkkllllmmmmnnnoooopppqqqqqqqqqqqrsssttttttttvxxxxxyyzzzzz"
        self.assertEqual(s.customSortString(S,T), Expected)

if __name__ == "__main__":
    unittest.main()
