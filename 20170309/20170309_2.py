# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        q.append(root)
        ans = root
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if i == 0:
                    ans = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return ans.val

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
        vals = [2,1,3]
        trees = makeTree(vals)
        self.assertEqual(s.findBottomLeftValue(trees), 1)
        vals = [1,2,3,4,None,5,6,None,None,None,None,7]
        trees = makeTree(vals)
        self.assertEqual(s.findBottomLeftValue(trees), 7)

if __name__ == "__main__":
    unittest.main()
