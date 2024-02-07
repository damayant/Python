from typing import Optional

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None

class Solution : 
    def isSameTree(self,p:Optional[TreeNode], q:Optional[TreeNode])->bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val !=  q.val :
            return False
        
        left_bool_result = self.isSameTree(p.left,q.left)
        right_bool_result =  self.isSameTree(p.right,q.right)

        return left_bool_result and right_bool_result 
        