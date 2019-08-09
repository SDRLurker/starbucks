# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode):
        cur = root
        q = []
        d = {}
        q.append(cur)
        if not cur:
            return []
        while q:
            p = q.pop(0)
            d[p.val] = d.get(p.val, 0) + 1
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        items = sorted(d.items(), key=lambda v:(v[1],v[0]), reverse=True)
        return [item[0] for item in items if item[1] == items[0][1]]

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
        vals = [1,None,2,None,None,2]
        trees = makeTree(vals)
        s = Solution()
        self.assertEqual(s.findMode(trees), [2])
        vals = [1,None,2]
        trees = makeTree(vals)
        self.assertEqual(s.findMode(trees), [2, 1])
        self.assertEqual(s.findMode(None), [])

if __name__ == "__main__":
    unittest.main()
