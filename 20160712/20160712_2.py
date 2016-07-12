# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = []
        self.r = []
            
    def getLeft(self, left):
        # when left is None, we can't get left.left by runtime error.
        self.getLeft(left.left)
        self.getLeft(left.right)
        if left:
            self.l.append(left.val)
        else:
            self.l.append("")
            
    def getRight(self, right):
        self.getRight(right.right)
        self.getRight(right.left)
        if right:
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
