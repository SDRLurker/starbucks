# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def in_order(self, node):
        if node.left:
            self.in_order(node.left)
        self.vals.append(node.val)
        if node.right:
            self.in_order(node.right)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.vals = []
        self.in_order(root)
        for i in range(len(self.vals)-1):
            if self.vals[i] >= self.vals[i+1]:
                return False
        return True

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
        s = Solution()
        self.assertEqual(s.isValidBST(None), True)
        vals = [2,1,3]
        trees = makeTree(vals)
        self.assertEqual(s.isValidBST(trees), True)
        vals = [5,1,4,None,None,3,6]
        trees = makeTree(vals)
        self.assertEqual(s.isValidBST(trees), False)

if __name__ == "__main__":
    unittest.main()
