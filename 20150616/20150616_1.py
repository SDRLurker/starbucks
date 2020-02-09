class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        a = (C-A) * (D-B)
        b = (G-E) * (H-F)        
        
        left = max(A,E)
        right = min(C,G)
        top = min(D,H)
        bottom = max(B,F)       
        
        overlap = 0
        if left < right and bottom < top:
            overlap = (right - left) * (top - bottom)
            if overlap <= 0:
                overlap = 0

        return a + b - overlap

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.computeArea(-3,0,3,4,0,-1,9,2), 45)
        self.assertEqual(s.computeArea(0,0,0,0,-1,-1,1,1), 4)
        self.assertEqual(s.computeArea(-2,-2,2,2,3,3,4,4), 17)

if __name__ == "__main__":
    unittest.main()
