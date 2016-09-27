# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        s = 0
        if root.left and not root.left.left and not root.left.right:
            s += root.left.val
        if root.left:
            s += self.sumOfLeftLeaves(root.left)
        if root.right:
            s += self.sumOfLeftLeaves(root.right)
        return s

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

s = Solution()
vals = [3,9,20,None,None,15,7]
root = makeTree(vals)
print("%35s %10s %10s" % ("input", "Expected", "Result"))
print("%35s %10d %10d" % (vals, 24, s.sumOfLeftLeaves(root))) 
