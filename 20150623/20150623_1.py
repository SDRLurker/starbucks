# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        if not root:
            return 0
        cnt = 0
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            cnt += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return cnt

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
        vals = [1,2,3,4,5,6]
        trees = makeTree(vals)
        s = Solution()
        self.assertEqual(s.countNodes(trees), 6)

if __name__ == "__main__":
    unittest.main()
