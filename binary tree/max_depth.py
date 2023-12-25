from collections import deque


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right =  None


class Solution:
    def maxDepth(root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        element_q = deque() 
        element_q.append(root)
        number_level = 0

        while True :
            node_count_at_level = len(element_q)
            if (node_count_at_level == 0) :
                return number_level
            
            while (node_count_at_level>0):
                element = element_q.popleft()

                if element is not None:
                    if(element.left is not None):
                        element_q.append(element.left)
                    if(element.right is not None):
                        element_q.append(element.right)
                    
                    node_count_at_level -= 1
            
            number_level+= 1

        return number_level

    root = None
    # root = TreeNode(0)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.left.left =  None
    # root.left.right =  None
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    # root.right.right.left =  TreeNode(3)
    # root.right.right.right =  TreeNode(1)

    print(maxDepth(root))
            
