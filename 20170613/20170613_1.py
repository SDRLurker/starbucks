# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

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

def makeArray(tree):
    q = []
    arr = []
    if tree:
        q.append(tree)
        while q:
            t = q.pop(0)
            arr.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
    return arr

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        vals = [1,3,2,5]
        t1 = makeTree(vals)
        vals = [2,1,3,None,4,None,7]
        t2 = makeTree(vals)
        vals = [3,4,5,5,4,None,7]
        t3 = makeTree(vals)
        s = Solution()
        self.assertEqual(makeArray(s.mergeTrees(t1, t2)), makeArray(t3))

if __name__ == "__main__":
    unittest.main()
