from collections import OrderedDict

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = "1"
        for _ in range(1, n):
            cnt_dic = OrderedDict()
            rr = ""
            for i, c in enumerate(r):
                if i > 0 and c != r[i-1]:
                    for k in cnt_dic:
                        rr += str(cnt_dic[k])
                        rr += str(k)
                    cnt_dic = OrderedDict()
                cnt_dic[c] = cnt_dic.get(c, 0) + 1
            for k in cnt_dic:
                rr += str(cnt_dic[k])
                rr += str(k)
            r = rr
        return r

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.countAndSay(1), "1")
        self.assertEqual(s.countAndSay(2), "11")
        self.assertEqual(s.countAndSay(3), "21")
        self.assertEqual(s.countAndSay(4), "1211")
        self.assertEqual(s.countAndSay(5), "111221")
        self.assertEqual(s.countAndSay(6), "312211")

if __name__ == "__main__":
    unittest.main()
