#difference between lca and lcaII is that in lca II you can have a node either p or q  which does not exist in the tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_found = False
        q_found = False
        stack = [root]
        parent ={root:None}
        while stack != []:
            node = stack.pop()
            if node == p:
                p_found = True
            if node == q:
                q_found = True
            if node.left is not None:
                parent[node.left] = node
                stack.append(node.left)
            if node.right is not None:
                parent[node.right] = node
                stack.append(node.right)

        if p_found == False or q_found == False:
            return 

        ancestor = set()
        while p :
            ancestor.add(p)
            p = parent[p]

        while q not in ancestor:
            q = parent[q]     

        return q 