class TreeNode:
    def __init__(self) -> None:
        self.val=0
        self.left=None
        self.right=None

class Solution:
    def flatten(self,root:TreeNode)->None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        node=root
        while node:
            # If the node has a left child
            if node.left:
                # Find the rightmost node of the left subtree
                rightmost=node.left # find the rightmost node of the left subtree
                while rightmost.right:
                    rightmost=rightmost.right
                
                # rewire the connections
                rightmost.right=node.right # append the right subtree to the rightmost node of the left subtree
                node.right=node.left
                node.left=None
            
            # move on to the right side of the tree
            node=node.right