# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res        
        q = []
        q.append(root)
        while q:
            level = []
            while q:
                node = q.pop(0)
                level.append(node)
            res.insert(0, [node.val for node in level])
            for node in level:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

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
        vals = [3,9,20,None,None,15,7]
        trees = makeTree(vals)
        s = Solution()
        self.assertEqual(s.levelOrderBottom(trees), [[15,7],[9,20],[3]])

if __name__ == "__main__":
    unittest.main()
