class Solution:
    def replaceWords(self, dict, sentence):
        l_dic = {}
        for w in dict:
            l_dic[w[0]] = l_dic.get(w[0], set())
            l_dic[w[0]].add(w)
        answer = []
        for w in sentence.split():
            isin_set = False
            if w[0] in l_dic:
                for sw in l_dic[w[0]]:
                    if w[:len(sw)] == sw:
                        isin_set = True
                        answer.append(sw)
                        break
            if not isin_set:
                answer.append(w)
        return " ".join(answer)

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        dic = ["cat","bat","rat"]
        sentence = "the cattle was rattled by the battery"
        result = "the cat was rat by the bat"
        self.assertEqual(s.replaceWords(dic, sentence), result)

if __name__ == "__main__":
    unittest.main()
