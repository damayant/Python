from typing import Optional


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None
class Solution:
    def lowestCommonAncestor(root,p,q):
        #stack for tree traversal
        stack =[root]

        #dictionary for parent pointers
        parent = {root : None}

        #iterate until we find both nodes p and q
        while p not in parent or q not in parent :
            node =  stack.pop()
            # while traversing the tree
            # keep saving the parent pointers
            if node.left : 
                parent[node.left] =  node 
                stack.append(node.left)
            if node.right :
                parent[node.right] =  node
                stack.append(node.right)
        
        #ancestors set for node p
        ancestors  =  set() #remember to have it a set next time revise not an array

        #process all ancestors for node p using parent pointers 
        while p : 
            ancestors.add(p)
            p =  parent[p]
        
        #the first ancestor of q which appears in 
        #p's ancestor set() is their LCA
        while q not in ancestors:
            q = parent[q]
        print(q.val)
        return q


    root  = TreeNode(3)
    root.left =  TreeNode(5)
    p = root.left
    root.right =  TreeNode(1)
    root.left.left = TreeNode(6) 
    root.left.right =  TreeNode(2)
    q = root.left.right
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    # q = root.right
    root.right.left =  TreeNode(0)
    root.right.right =  TreeNode(8)

    lowestCommonAncestor(root,p,q)