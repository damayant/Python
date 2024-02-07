from typing import Optional


class ListNode:
    def __init__(self,x) -> None:
        self.val = x
        self.next = None

class Solution :
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 : return l2
        if l1 and l2 is None: return l1

        new_head = ListNode(0)
        carry , sum = 0 , 0

        if l1.next is None and l2.next is None : 
            sum = l1.val + l2.val
            if sum <10 :
                new_head = ListNode(sum)
            else:
                carry = sum //10
                rem = sum%10
                new_head = ListNode(rem)
                new_head.next = ListNode(carry)
            return new_head

        dummy_head = new_head

        while l1 or l2 :
            if l1 is not None and l2 is not None :
                sum = l1.val + l2.val + carry
            if l1 and l2 is None:
                sum = l1.val + carry
            if l1 is None and l2 :
                sum = l2.val + carry
            if sum >=0 and sum <10 :
                dummy_head.next = ListNode(sum)
                carry = 0
            elif sum >=10 :
                carry = sum//10
                rem = sum%10
                dummy_head.next = ListNode(rem)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            dummy_head = dummy_head.next
        
        if sum >9 and carry >0 :
            dummy_head.next = ListNode(carry)

        return new_head.next
