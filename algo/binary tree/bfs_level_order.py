# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []
        level_order_nodes = []
        node_count_at_current_level = 0
        if root:
            q.append(root)
            result.append([root.val])
            node_count_at_current_level = len(q)
        while q:
            if node_count_at_current_level == 0 :
                result.append(level_order_nodes)
                level_order_nodes = []
            node_count_at_current_level = len(q)
            while(node_count_at_current_level>0):
                element = q.popleft()
                if element is not None:
                    if element.left is not None:
                        level_order_nodes.append(element.left.val)
                        q.append(element.left)
                    if element.right is not None:
                        level_order_nodes.append(element.right.val)
                        q.append(element.right)
                    node_count_at_current_level -= 1
        return result