from typing import Counter, Optional

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next =  next

class Solution: 
    #this solution passes all test cases with O(N) time complexity and O(1) space complexity
    def rotateRight(head:Optional[ListNode], k: int):
        #base cases 
        if not head :
            return None
        if not head.next :
            return head
        
        #close the linked-list into a ring
        old_tail = head
        n = 1
        while old_tail.next :
            old_tail =   old_tail.next
            n+= 1
        old_tail.next =  head

        #find new tail : (n-k%n-1)th node
        #add new  head : (n-k%n)th node
        new_tail =  head
        for i in range(n-k%n-1):
            new_tail = new_tail.next
        new_head = new_tail.next

        #break the ring
        new_tail.next = None

        return new_head

    #this solution DOES NOT pass all test cases
    def withOneIteration(head:Optional[ListNode], k: int):
            dummy = ListNode(0,head)

            first_ptr , second_ptr = dummy , dummy
            left_prev = None

            for i in range(k):
                if second_ptr.next is not None :
                    left_prev = second_ptr
                    second_ptr =  second_ptr.next
                else :
                    new_head = second_ptr
                    left_prev.next = None
                    new_head.next = dummy.next
                    return new_head
                    

            while second_ptr.next is not None:
                first_ptr =  first_ptr.next
                second_ptr =  second_ptr.next
            
            new_head = first_ptr.next
            first_ptr.next = None

            dummy_new_head =  new_head

            while dummy_new_head.next is not None:
                dummy_new_head =  dummy_new_head.next

            dummy_new_head.next  = dummy.next

            result_head =  new_head

            while new_head is not None:
                print(new_head.val)
                new_head = new_head.next

            return result_head

            # while(new_head is not None):
            #     print(new_head.val)
            #     new_head =  new_head.next  










    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next =  ListNode(3)
    # head.next.next.next =  ListNode(4)
    # head.next.next.next.next =  ListNode(5)
    # head.next.next.next.next.next = None

    head = ListNode(0)
    head.next =  ListNode(1)
    head.next.next =  ListNode(2)


    



    rotateRight(head,k=4)
