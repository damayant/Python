from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None

class Solution:
    def invertTree(root:Optional[TreeNode])->Optional[TreeNode]:
        if root is None:
            return None
        
        tree_node_q = deque()
        tree_node_q.append(root)

        while(len(tree_node_q) > 0):
            popped_tree_node = tree_node_q.popleft()

            #swap nodes
            temp  =  popped_tree_node.left
            popped_tree_node.left = popped_tree_node.right
            popped_tree_node.right  = temp

            #add  left and right child nodes of popped tree node to q
            if(popped_tree_node.left is not None):
                tree_node_q.append(popped_tree_node.left)
            if(popped_tree_node.right is not None):
                tree_node_q.append(popped_tree_node.right)
        print(root)
        return root


    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left =  TreeNode(1)
    root.left.right =  TreeNode(3)
    root.left.left.left =  None
    root.left.left.right =  None
    root.left.right.left =  None
    root.left.right.right = None
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root.right.left.left =  None
    root.right.left.right  = None
    root.right.right.left = None
    root.right.right.right = None

    invertTree(root)
