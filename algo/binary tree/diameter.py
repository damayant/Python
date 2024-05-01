class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None


class Solution:
    def diameterOfBinaryTree(root:TreeNode):
        res  =  [0]

        def dfs(root):
            if not root: 
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0],2+left+right)

            return 1+max(left,right)

        dfs(root)
        return res[0]
    
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    # root.left.left =   TreeNode(4)
    # root.left.right =  TreeNode(5)

    print(diameterOfBinaryTree(root))
