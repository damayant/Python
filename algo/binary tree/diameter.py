
#diameter of binary tree:Longest path between any two nodes in the tree, which doesn't necessarily pass through the root.

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # Update the diameter at this node
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return the height of the current node
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.diameter

    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left =   TreeNode(4)
    root.left.right =  TreeNode(5)

    print(diameterOfBinaryTree(root))
