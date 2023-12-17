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
        


        

        
       

        



        
    

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next =  ListNode(3)
    head.next.next.next =  ListNode(4)
    head.next.next.next.next =  ListNode(5)
    head.next.next.next.next.next = None

    removeNthFromEnd(head , n = 2)





