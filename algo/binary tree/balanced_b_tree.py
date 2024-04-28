from typing import Optional


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None
class Solution:
    # Compute the tree's height via recursion
    def height(self,root:TreeNode)->int:
        # An empty tree has height -1
        if root is None:
            return -1
        max_height = max(self.height(root.left),self.height(root.left))
        return 1+ max_height
    
    # def isBalanced(root:TreeNode)->bool:
    #     # An empty tree satisfies the definition of a balanced tree
    #     if root is None:
    #         return True
    #     # Check if subtrees have height within 1. If they do, check if the
    #     # subtrees are balanced
    #     return ( abs(height(root.left)-height(root.right))>2  # type: ignore
    #             and isBalanced(root.right) # type: ignore
    #             and isBalanced(root.left)) # type: ignore
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right =  TreeNode(20)
    root.right.left  = TreeNode(15)
    root.right.right = TreeNode(7)

    height(root)
    