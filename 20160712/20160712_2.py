# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.l = []
        self.r = []
            
    def getLeft(self, left):
        if left:
            self.getLeft(left.left)
            self.getLeft(left.right)
            self.l.append(left.val)
        else:
            self.l.append("")
            
    def getRight(self, right):
        if right:
            self.getRight(right.right)
            self.getRight(right.left)
            self.r.append(right.val)
        else:
            self.r.append("")
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if (root.left == None and root.right) or (root.right == None and root.left):
            return False
        self.l = []
        self.r = []
        self.getLeft(root.left)
        self.getRight(root.right)
        return self.l == self.r

def makeTree(vals):
    nodes = []
    for i in vals:
        node = TreeNode(i)
        nodes.append(node)
    i = 0
    while i < len(vals):
        nodes[i].left = nodes[(i+1) * 2 - 1] if (i+1) * 2 - 1 < len(vals) else None
        nodes[i].right = nodes[(i+1) * 2] if (i+1) * 2 < len(vals) else None
        i += 1
    return nodes[0]

s = Solution()
vals = [1,2,2,3,4,4,3]
root = makeTree(vals)
print "%35s %10s %10s" % ("input", "Expected", "Result")
print "%35s %10s %10s" % (vals, "True", s.isSymmetric(root)) 
vals = [1,2,2,None,3,None,3]
root = makeTree(vals)
print "%35s %10s %10s" % (vals, "False", s.isSymmetric(root)) 
