# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = []
        lev = max_lev = 0
        a = {}
        c = {}
        l = []
        if root:
            q.append((root, lev))
        while len(q) > 0:
            node, lev = q.pop(0)
            if node.left:
                q.append((node.left, lev+1))
            if node.right:
                q.append((node.right, lev+1))
            a[lev] = a.get(lev, 0) + node.val
            c[lev] = c.get(lev, 0) + 1
        for i in range(len(a)):
            l.append(float(a[i])/float(c[i]))
        return l

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
        vals = [3,9,20,15,7]
        trees= makeTree(vals)
        s = Solution()
        self.assertEqual(s.averageOfLevels(trees), [3.00000,14.50000,11.00000])

if __name__ == "__main__":
    unittest.main()
