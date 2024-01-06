from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution : 
    def partition(head:Optional[ListNode], x:int)->Optional[ListNode]:
        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save heads of the two lists 
        before = before_head = ListNode(0)
        after =  after_head = ListNode(0) 

        while head :
            #if the original list node is lesser than X assign it to the before list
            if head.val < x :
                before.next = head
                before = before.next
            else :
                #if the original list node is greater than or equal to X assign to after list
                after.next = head
                after =  after.next
            
            #move ahead in the original list
            head = head.next

        #last node of "after" list would also be ending node of the reformed list
        after.next = None

        #once all the nodes are correctly assigned to the two lists ,
        #combine them to form a single list which would be returned 
        before.next = after_head.next

        return before_head.next

    head  = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next =  ListNode(2)
    head.next.next.next.next =  ListNode(5)
    head.next.next.next.next.next =  ListNode(2)

    partition(head,x=3)