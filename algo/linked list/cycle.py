from typing import Optional


class ListNode:
    def __init__(self,x) -> None:
        self.val = x
        self.next = None
    
class Solution:
    def hasCycle(head:Optional[ListNode])->bool:
        nodes_seen = {}
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen[head] =  head.val
            head =  head.next
        return False

    head = ListNode(3)
    head.next =  ListNode(2)
    head.next.next =  ListNode(0)
    head.next.next.next =  ListNode(-4)
    head.next.next.next.next = head.next
    print(hasCycle(head))