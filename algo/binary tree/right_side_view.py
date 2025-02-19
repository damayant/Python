from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)
        while q:
            level_size = len(q)
            while level_size > 0:
                current_node = q.popleft()
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
                level_size -= 1
            if q:
                result.append(q[-1].val)
        return result