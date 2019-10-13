# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.pre_list = []
        if root:
            self.preorder(root)
        return self.pre_list
    def preorder(self, root):
        if root:
            self.pre_list.append(root.val)
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)
        
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
        vals = [1,None,2,None,None,3,None]
        trees = makeTree(vals)
        s = Solution()
        self.assertEqual(s.preorderTraversal(trees), [1,2,3])
        self.assertEqual(s.preorderTraversal(None), [])

if __name__ == "__main__":
    unittest.main()
