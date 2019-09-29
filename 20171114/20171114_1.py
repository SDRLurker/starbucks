# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        self.routes = []
        if root:
            a = [0 for _ in range(1000)]
            a[0] = root.val
            self.get_path(root, a, 0)
        return self.routes
    def get_path(self, node, a, k):
        if self.is_solution(node, a, k):
            self.routes.append("->".join([str(v) for v in a[:k+1]]))  
        k = k + 1
        nodes = self.get_candidates(node, a, k)
        for node in nodes:
            a[k] = node.val
            self.get_path(node, a, k)
    def is_solution(self, node, a, k):
        return not node.left and not node.right
    def get_candidates(self, node, a, k):
        nodes = []
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
        return nodes

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
        vals = [1,2,3,None,5]
        trees = makeTree(vals)
        s = Solution()
        self.assertEqual(s.binaryTreePaths(trees), ["1->2->5","1->3"])
        self.assertEqual(s.binaryTreePaths(None), [])

if __name__ == "__main__":
    unittest.main()
