class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.answer = []
        a = [0 for _ in range(len(graph))]
        self.backtrack(graph, a, 0)
        return self.answer
    
    def backtrack(self, graph, a, k):
        if self.is_solution(graph, a, k):
            self.answer.append(a[:k+1])
        k = k + 1
        c = self.candidate(graph, a, k)
        for i in range(len(c)):
            a[k] = c[i]
            self.backtrack(graph, a, k)
    
    def candidate(self, graph, a, k):
        candidates = []
        for t in graph[a[k-1]]:
            candidates.append(t)
        return candidates
    
    def is_solution(self, graph, a, k):
        if a[k] == len(graph) - 1:
            return True
        return False

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        in_lst = [[1,2], [3], [3], []]
        out_lst = [[0,1,3],[0,2,3]]
        self.assertEqual(s.allPathsSourceTarget(in_lst), out_lst)

if __name__ == "__main__":
    unittest.main()
