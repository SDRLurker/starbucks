class Solution:
    def calPoints(self, ops):
        scores = []
        for op in ops:
            if op == "C":
                scores.pop()
            elif op == "D":
                scores.append(scores[-1] * 2)
            elif op == "+":
                scores.append(scores[-2]+scores[-1])
            else:
                scores.append(int(op))
        return sum(scores)

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.calPoints(["5","2","C","D","+"]), 30)
        self.assertEqual(s.calPoints(["5","-2","4","C","D","9","+","+"]), 27)

if __name__ == "__main__":
    unittest.main()
