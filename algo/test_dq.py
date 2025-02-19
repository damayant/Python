class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def test(root: TreeNode) -> int:
        q=deque()
        q.append(root)

        while len(q)>0:
            node=q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
    
    test(root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6))))