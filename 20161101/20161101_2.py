# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def route_node(self, node, t, r_list):
        if not node:
            return False
        if node == t or self.route_node(node.left,t,r_list) or self.route_node(node.right,t,r_list):
            r_list.append(node)
            return True
        return False
    def lowestCommonAncestor(self, root, p, q): 
        p_route = []
        self.route_node(root, p, p_route)
        q_route = []
        self.route_node(root, q, q_route)
        p_route = p_route[::-1]
        q_route = q_route[::-1]
        if len(p_route) > len(q_route):
            p_route, q_route = q_route, p_route
        i=0
        while i < len(p_route):
            if p_route[i] == q_route[i]:
                i+=1
            else:
                break
        return p_route[i-1]

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
print("%40s %5s %5s %10s %10s" % ("input", "p", "q", "Expected", "Result"))
print("%40s %5d %5d %10d %10s" % (vals, vals[1], vals[2], vals[0], s.lowestCommonAncestor(trees[0], trees[1], trees[2]).val)) 
print("%40s %5d %5d %10d %10s" % (vals, vals[1], vals[10], vals[1], s.lowestCommonAncestor(trees[0], trees[1], trees[10]).val)) 
