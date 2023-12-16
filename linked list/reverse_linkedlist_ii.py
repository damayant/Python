from typing import Counter, Optional


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next =  next

class Solution:
    def reverse(head:Optional[ListNode],left:int,right:int)->Optional[ListNode]:
        
        dummy  = ListNode(0, head)

        left_prev  = dummy
        current = head
        #reach node at position left
        for i in range(left-1):
            left_prev = current
            current =  current.next
        
        previous = None
        #now current = left , left_prev= node before left
        #reverse from left to right
        for i in range(right-left+1):
            temp_next = current.next
            current.next =  previous
            previous = current
            current = temp_next
        #update pointers
        left_prev.next.next = current #current is node after 'right'
        left_prev.next = previous #prev is right

        print_dummy =  dummy
        while(print_dummy!= None):
            print(print_dummy.val)
            print_dummy =  print_dummy.next
        return dummy.next


    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next =  ListNode(3)
    head.next.next.next =  ListNode(4)
    head.next.next.next.next =  ListNode(5)
    reverse(head , left = 2, right = 4)