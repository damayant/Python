#definition of binary tree node
import math
from typing import Optional

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution :
    def isValidBST(root:Optional[TreeNode])->bool :
        def validate(node,low=-math.inf,high=math.inf):
            #print('current node dets:',node.val, node.left,node.right)
            #empty trees are valid bsts
            if not  node:
                return True
            
            #current node's value must be between low and high
            if node.val <= low or node.val >=high:
                return  False
            
            return (validate(node.right,node.val,high)) and (validate(node.left,low,node.val))
        return validate(root)


    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(7)

    print(isValidBST(root))

