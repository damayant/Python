
#max depth : Longest path from root to any leaf node (count of nodes or edges)

from collections import deque


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None


from collections import deque

class Solution:
    def maxDepth(self, root) -> int:
        # Entry point: computes the maximum depth of a binary tree
        if root is None:
            return 0
        if self._is_leaf_node(root):
            return 1

        return self._calculate_tree_depth(root)

    def _is_leaf_node(self, node) -> bool:
        # Helper to check if a node is a leaf (no children)
        return node.left is None and node.right is None

    def _calculate_tree_depth(self, root) -> int:
        """
        Uses level-order traversal (BFS) to calculate the depth of the tree.
        """
        node_queue = deque()
        node_queue.append(root)
        depth_counter = 0

        while node_queue:
            current_level_node_count = len(node_queue)

            for _ in range(current_level_node_count):
                current_node = node_queue.popleft()

                self._enqueue_child_if_present(current_node.left, node_queue)
                self._enqueue_child_if_present(current_node.right, node_queue)

            depth_counter += 1

        return depth_counter

    def _enqueue_child_if_present(self, child, queue: deque):
        # Adds a child node to the queue if it's not None
        if child is not None:
            queue.append(child)

    
    def recursiveSolution(self,root):
        if not  root:
            return 0
        return 1+max(self.recursiveSolution(root.left),self.recursiveSolution(root.right))


    root = None
    root = TreeNode(0)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left =  None
    root.left.right =  None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.left =  TreeNode(3)
    root.right.right.right =  TreeNode(1)

    print(maxDepth(root))

    #https://www.youtube.com/watch?v=bkxqA8Rfv04&pp=ygUXZGlhbWV0ZXIgb2YgYmluYXJ5IHRyZWU%3D
            
