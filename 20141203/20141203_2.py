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
        :rtype: List[List[int]]
        """
        queue = []
        if root is not None:
            queue.append((root, sum, [root.val]))
        resultList = []
        while len(queue) > 0:
            root, currentSum, currentList = queue.pop(0)
            diff = currentSum - root.val
            
            if diff == 0 and root.left == None and root.right == None:
                resultList.append(currentList)
            
            if root.left != None:
                queue.append((root.left, diff, currentList + [root.left.val]))
            if root.right != None:
                queue.append((root.right, diff, currentList + [root.right.val]))
        
        return resultList

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
        vals = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
        trees = makeTree(vals)
        s = Solution()
        self.assertEqual(s.pathSum(trees,22), [[5,4,11,2],[5,8,4,5]])
        vals = [-2,None,-3]
        trees = makeTree(vals)
        self.assertEqual(s.pathSum(trees,-5), [[-2,-3]])

if __name__ == "__main__":
    unittest.main()
