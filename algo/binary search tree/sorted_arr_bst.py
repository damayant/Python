class TreeNode:
    def __init__(self,val):
        self.val=val 
        self.left=None 
        self.right=None

def sorted_list_to_bst(nums):
    #base case: no elements
    if not nums:
        return None 
    #middle element->root
    mid=len(nums)//2
    root=TreeNode(nums[mid])

    root.left=sorted_list_to_bst(nums[:mid])
    root.right=sorted_list_to_bst(nums[mid+1:])

    return root 

#helper function to print tre(in-order)
def inorder_traversal(node):
    if not node:
        return []
    return inorder_traversal(node.left)+[node.val]+inorder_traversal(node.right)


nums=[-10,-3,0,5,9]

root=sorted_list_to_bst(nums)

print(inorder_traversal(root))