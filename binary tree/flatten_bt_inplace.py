from typing import Optional


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None

class Solution:
    
    def flatten(root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Handle the null scenario
        if not root:
            return None
        
        node = root
        while node:
            
            # If the node has a left child
            if node.left:
                
                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            
            # move on to the right side of the tree
            node = node.right



    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = None
    root.right = TreeNode(5)
    root.right.left = None
    root.right.right = TreeNode(6)

    flatten(root)