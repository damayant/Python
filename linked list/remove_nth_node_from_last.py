from typing import Optional


from typing import Counter, Optional


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next =  next
class Solution:
    def removeNthFromEnd(head:Optional[ListNode],n:int)->Optional[ListNode]:
        dummy = head 
        count = 0
        while(dummy!=None):
            count += 1
            dummy =  dummy.next
        count -=  1

        temp_prev = ListNode(0)
        result = ListNode(0)
        result.next = head
        dummy = result.next

        for i in range(count-n+1):
            temp_prev = dummy
            dummy = dummy.next

        temp_prev.next =  temp_prev.next.next

        return result.next

    def withOneIteration(head:Optional[ListNode],n:int)->Optional[ListNode]:
        #initialise the dummy node 
        dummy = ListNode(0)
        dummy.next = head

        #initialise the ptrs to point to dummy node
        first_ptr = dummy
        second_ptr = dummy

        #shift the secnd_ptr to start n steps ahead of first ptr
        for i in range(n):
            second_ptr =  second_ptr.next

        #check while the second_ptr.next is not null , shift the first and second ptr by 1 step each
        while second_ptr.next is not None:
            first_ptr =  first_ptr.next
            second_ptr = second_ptr.next
        
        #when the second_ptr.next reaches null , the first ptr will be at a position 
        #such that the next node to the firts ptr is the one that needs to be removed
        first_ptr.next = first_ptr.next.next

        return dummy.next
        


        

        
       

        



        
    

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next =  ListNode(3)
    head.next.next.next =  ListNode(4)
    head.next.next.next.next =  ListNode(5)
    head.next.next.next.next.next = None

    withOneIteration(head , n = 2)





