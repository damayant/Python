# https://www.youtube.com/watch?v=olbiZ-EOSig
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val 
        self.left=left 
        self.right=right 

class Solution:
    def isComplete(self,root:Optional[TreeNode]):
        q=deque([root])

        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                while q:
                    if q.popleft():
                        return False 
        return True 
        