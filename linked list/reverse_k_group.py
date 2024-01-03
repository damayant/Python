from typing import Counter, Optional


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next =  next

def reverseKGroup(head:Optional[ListNode], k: int)->Optional[ListNode]:
    dummy = ListNode(0,head)
        
    current =  dummy.next
    start_node , end_node =  None, None

    while current is not None: 
        start_node =  current
        for i in range(k):
            if current is not None:
                end_node =  current
            else:
                return dummy.next
            current = current.next
            reverse(start_node,end_node)

    while(dummy is not None):
        (dummy.val)
        dummy =  dummy.next
    return dummy.next
             
def reverse(node_start:Optional[ListNode], node_end:Optional[ListNode])->Optional[ListNode]:
    dummy = node_start
    prev = None

    while dummy!= node_end :
        temp = dummy.next
        dummy.next =  prev
        prev = dummy
        dummy = temp

    return prev
    


  
        
   
 
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next =  ListNode(3)
    head.next.next.next =  ListNode(4)
    head.next.next.next.next =  ListNode(5)

    reverseKGroup(reverseKGroup, head, k= 3)