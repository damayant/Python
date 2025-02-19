class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self,root:TreeNode)->int:
        def dfs(node,sum):
            if not node:
                return 0
            
            sum = sum*10 + node.val
            if not node.left and not node.right:
                return sum
            return dfs(node.left,sum)+dfs(node.right,sum)
        return dfs(root,0)