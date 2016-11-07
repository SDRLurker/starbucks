# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.cnt = 0
        if not root:
            return self.cnt
        a = [0 for _ in range(1001)]
        a[0] = root
        self.backtrack(a, sum, 0)
        return self.cnt
        
    def backtrack(self, a, sum, k):
        cnt = self.is_solution(a, sum, k)
        if cnt > 0:
            self.cnt += cnt
        k = k + 1
        c = self.candidate(a, sum, k)
        for i in range(len(c)):
            a[k] = c[i]
            self.backtrack(a, sum, k)
    
    def is_solution(self, a, sum, k):
        c = 0
        s = 0
        i = k
        while i>=0:
            s += a[i].val
            if s == sum:
                c += 1
            i -= 1
        return c
    
    def candidate(self, a, sum, k):
        c = []
        if a[k-1].left:
            c.append(a[k-1].left)
        if a[k-1].right:
            c.append(a[k-1].right)
        return c

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
vals = [10,5,-3,3,2,None,11,3,-2,None,1]
trees = makeTree(vals)
print("%50s %5s %10s %10s" % ("input", "sum", "Expected", "Result"))
print("%50s %5d %10d %10s" % (vals, 8, 3, s.pathSum(trees[0], 8))) 
print("%50s %5d %10d %10s" % ([], 1, 0, s.pathSum(None, 1))) 
vals = [0,1,1]
trees = makeTree(vals)
print("%50s %5d %10d %10s" % (vals, 1, 4, s.pathSum(trees[0], 1))) 
vals = [1,None,2,None,None,None,3]
trees = makeTree(vals)
print("%50s %5d %10d %10s" % (vals, 3, 2, s.pathSum(trees[0], 3))) 
