# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode):
        max_row = []
        cur = root
        q = []
        if not root:
            return max_row
        q.append((cur,0))
        while q:
            cur, lvl = q.pop(0)
            if len(max_row) > lvl:
                max_row[lvl] = max(cur.val, max_row[lvl])
            else:
                max_row.append(cur.val)
            if cur.left:
                q.append((cur.left,lvl+1))
            if cur.right:
                q.append((cur.right,lvl+1))
        return max_row

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
        vals = [1,3,2,5,3,None,9]
        trees = makeTree(vals)
        s = Solution()
        self.assertEqual(s.largestValues(trees), [1,3,9])
        self.assertEqual(s.largestValues(None), [])

if __name__ == "__main__":
    unittest.main()
