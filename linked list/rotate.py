from typing import Counter, Optional

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next =  next

class Solution: 
    def rotateRight(head:Optional[ListNode], k: int):
        dummy = head
        count = 0

        #count the size of the LL
        while(dummy is not None):
            count += 1
            dummy =  dummy.next
        count -= 1

        temp_prev =  ListNode(0)
        result =  ListNode(0)

        result.next = head
        dummy = result.next

        #get the last node of the LL which will now point to null
        for i in range(count-k+1):
            temp_prev = dummy
            dummy =  dummy.next

        #point the new last node to  None
        temp_prev.next = None
        #copy the address of the new head
        new_head =  dummy
        #find the last node of the new rotated subarray which should point to the original head
        while(dummy.next is not  None):
            dummy = dummy.next
        
        #point the last node of the rotated LL to the original head
        dummy.next =  result.next

        while(new_head is not None):
            print(new_head.val)
            new_head =  new_head.next

        return new_head

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next =  ListNode(3)
    head.next.next.next =  ListNode(4)
    head.next.next.next.next =  ListNode(5)
    head.next.next.next.next.next = None


    rotateRight(head,k=2)
