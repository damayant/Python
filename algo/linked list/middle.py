from typing import Optional


class ListNode:
    def __init__(self,x) -> None:
        self.val = x
        self.next = None

class Solution :
    def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast =  fast.next.next
        
        return slow