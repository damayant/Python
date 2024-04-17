from typing import Optional

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(root:Optional[TreeNode])->int:
        node_values = []

        def dfs(node):
            if node is None:
                return 
            node_values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        node_values.sort()
        min_diff = 1e9
        for i in range(1,len(node_values)):
            min_diff = min(min_diff,node_values[i]-node_values[i-1])

        return min_diff
    
    root =TreeNode(4)
    root.right = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    print(getMinimumDifference(root))