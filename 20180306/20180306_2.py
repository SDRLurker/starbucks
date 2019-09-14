# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        """
        self.vals = []
        self.sortBST(root)
        m = 99999
        for i in range(len(self.vals)-1):
            m = min(m, abs(self.vals[i+1]-self.vals[i]))
        return m
    def sortBST(self, root):
        if root.left:
            self.sortBST(root.left)
        self.vals.append(root.val)
        if root.right:
            self.sortBST(root.right)

def makeTree(vals):
    nodes = []
    for i in vals:
        node = TreeNode(i)
        nodes.append(node)
    i = 0
    while i < len(vals):
        nodes[i].left = nodes[(i+1) * 2 - 1] if (i+1) * 2 - 1 < len(vals) and vals[(i+1) * 2 - 1] else None
        nodes[i].right = nodes[(i+1) * 2] if (i+1) * 2 < len(vals) and vals[(i+1) * 2] else None
        i += 1
    return nodes[0]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        vals = [4,2,6,1,3]
        trees = makeTree(vals)
        s = Solution()
        self.assertEqual(s.minDiffInBST(trees), 1)
        vals = [90,69,None,49,89,None,None,None,52]
        trees = makeTree(vals)
        self.assertEqual(s.minDiffInBST(trees), 1)

if __name__ == "__main__":
    unittest.main()
