from typing import List, Optional


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None

class Solution :
    def buildTree(self, preorder:List[int],inorder:List[int])->Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])

        return root

    
    buildTree(buildTree, preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
