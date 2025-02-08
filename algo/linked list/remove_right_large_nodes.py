#problem statement:https://leetcode.com/problems/remove-nodes-from-linked-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        dummy = ListNode(0,head)
        result = dummy
        current=head
        right_val=0
        while current is not None:
            if len(stack)==0:
                stack.append(current.val)
            else:
                if current.val < right_val :
                    stack.append(current.val)
                else:
                    while (current.val>right_val) and len(stack)!=0 :
                        stack.pop()
                        if(len(stack)!=0):
                            right_val =stack[-1]
                    stack.append(current.val)
            right_val=current.val
            current=current.next

        while len(stack)!=0:
            if dummy.next is not None:
                cur = dummy.next
                if cur.val != stack[0]:
                    dummy.next=dummy.next.next
                else:
                    dummy=dummy.next
                    stack.pop(0)
        
        return result.next
                 

        
