class Solution:
    def floodFill(self, image, sr, sc, newColor, oldColor = None):
        if oldColor is None:
            oldColor = image[sr][sc]
            self.check_set = set()
        image[sr][sc] = newColor
        self.check_set.add((sr,sc))
        y = len(image)
        x = len(image[0])
        if sc > 0 and sc < x and image[sr][sc-1] == oldColor and (sr,sc-1) not in self.check_set:
            self.floodFill(image, sr, sc-1, newColor, oldColor)
        if sc >= 0 and sc < x-1 and image[sr][sc+1] == oldColor and (sr,sc+1) not in self.check_set:
            self.floodFill(image, sr, sc+1, newColor, oldColor)
        if sr > 0 and sr < y and image[sr-1][sc] == oldColor and (sr-1,sc) not in self.check_set:
            self.floodFill(image, sr-1, sc, newColor, oldColor)
        if sr >= 0 and sr < y-1 and image[sr+1][sc] == oldColor and (sr+1,sc) not in self.check_set:
            self.floodFill(image, sr+1, sc, newColor, oldColor)
        return image
        
            
import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        i = [[1,1,1],[1,1,0],[1,0,1]]
        o = [[2,2,2],[2,2,0],[2,0,1]]
        self.assertEqual(s.floodFill(i, 1, 1, 2), o)
        i = [[0,0,0],[0,1,1]]
        o = [[0,0,0],[0,1,1]]
        self.assertEqual(s.floodFill(i, 1, 1, 1), o)

if __name__ == "__main__":
    unittest.main()
