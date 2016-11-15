# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def curDepth(self, root, d):
        if not root:
            return
        if self.d < d:
            self.d = d
        self.curDepth(root.left, d+1)
        self.curDepth(root.right, d+1)
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = 0
        self.curDepth(root, 1)
        return self.d

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
    return nodes

s = Solution()
vals = [3,5,1,6,2,0,8,None,None,7,4]
trees = makeTree(vals)
print("%40s %10s %10s" % ("input", "Expected", "Result"))
print("%40s %10d %10s" % (vals, 4, s.maxDepth(trees[0]))) 
