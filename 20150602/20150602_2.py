# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            p = stack.pop()
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
            p.left = None
            if len(stack) > 0:
                p.right = stack[-1]

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

# https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
COUNT = [10]  
ss = ""
# Function to print binary tree in 2D  
# It does reverse inorder traversal  
def print2DUtil(root, space) : 
    global ss
  
    # Base case  
    if (root == None) : 
        return
  
    # Increase distance between levels  
    space += COUNT[0] 
  
    # Process right child first  
    print2DUtil(root.right, space)  
  
    # Print current node after space  
    # count  
    #print()  
    ss += '\n'
    for i in range(COUNT[0], space): 
        #print(end=" ")  
        ss += " "
    #print(root.val)  
    ss += "%d\n" % root.val
  
    # Process left child  
    print2DUtil(root.left, space)  
  
# Wrapper over print2DUtil()  
def print2D(root) : 
    global ss
    ss = ""  
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)  
    return ss

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        i = []
        s.flatten(i)
        self.assertEqual(i, i)
        vals = [1,2,5,3,4,None,6]
        i = makeTree(vals)
        s.flatten(i)
        its = print2D(i)
        vals = [                       1,
                                    None,2,
                               None,None,None,3,
                     None,None,None,None,None,None,None,4,
 None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5,
 None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
 None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,6]
        o = makeTree(vals)
        ots = print2D(o)
        self.assertEqual(its, ots)

if __name__ == "__main__":
    unittest.main()
