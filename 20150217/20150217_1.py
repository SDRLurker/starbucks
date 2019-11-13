# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _solve(self, node, val):
        if not node:
            return
        if node and not node.left and not node.right:
            self.result += (val*10 + node.val)
            return        
        if node.left:
            self._solve(node.left, val*10 + node.val)
        if node.right:
            self._solve(node.right, val*10 + node.val)
            
            
    def sumNumbers(self, root):
        self.result = 0
        self._solve(root, 0)
        return self.result

def makeTree(vals):
    nodes = []
    for i in vals:
        node = TreeNode(i) if i is not None else None
        nodes.append(node)
    i = 0
    while i < len(vals):
        if nodes[i]:
            nodes[i].left = nodes[(i+1) * 2 - 1] if (i+1) * 2 - 1 < len(vals) and vals[(i+1) * 2 - 1] is not None else None
            nodes[i].right = nodes[(i+1) * 2] if (i+1) * 2 < len(vals) and vals[(i*1) * 2] is not None else None
            #print(i, nodes[i].val, (i+1) * 2 - 1, nodes[i].left.val if nodes[i].left else None, (i+1)*2, nodes[i].right.val if nodes[i].right else None)
        i += 1
    return nodes[0]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()

        vals = [1,2,3]
        trees = makeTree(vals)
        self.assertEqual(s.sumNumbers(trees), 25)

        vals = [4,9,0,5,1]
        trees = makeTree(vals)
        self.assertEqual(s.sumNumbers(trees), 1026)

        self.assertEqual(s.sumNumbers(None), 0)

        vals = [      2,
                     7, 4,
               None,4,  0,None,
          None,None,2,None,None,None,None,None,
None,None,None,None,1]
        trees = makeTree(vals)
        self.assertEqual(s.sumNumbers(trees), 27661)

if __name__ == "__main__":
    unittest.main()
