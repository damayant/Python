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

        
        result =  ListNode(0)

        result.next = head
        dummy = result.next
        temp_prev =  ListNode(0)

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

    def withOneIteration(head:Optional[ListNode], k: int):
            dummy = ListNode(0)
            dummy.next  = head

            first_ptr = dummy
            second_ptr = dummy

            for i in range(k):
                second_ptr =  second_ptr.next

            while second_ptr.next is not None:
                first_ptr =  first_ptr.next
                second_ptr =  second_ptr.next
            
            new_head = first_ptr.next
            first_ptr.next = None

            dummy_new_head =  new_head

            while dummy_new_head.next is not None:
                dummy_new_head =  dummy_new_head.next

            dummy_new_head.next  = dummy.next

            return new_head

            # while(new_head is not None):
            #     print(new_head.val)
            #     new_head =  new_head.next  










    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next =  ListNode(3)
    head.next.next.next =  ListNode(4)
    head.next.next.next.next =  ListNode(5)
    head.next.next.next.next.next = None


    



    withOneIteration(head,k=2)
