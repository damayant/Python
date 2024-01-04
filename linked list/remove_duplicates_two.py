from typing import Optional


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next =  next

class Solution :
    def deleteDuplicates(head:Optional[ListNode])->Optional[ListNode]:
        #sentinel
        sentinel = ListNode(0,head)

        #predecessor = last node
        #before the sublist of duplicates
        pred = sentinel

        while head :
            #if its the beginning of a duplicate sublist - skip all  duplicates
            if head.next and head.val == head.next.val :
                #move till end of duplicates sublist
                while head.next and head.val == head.next.val : 
                    head = head.next
                
                #skip all duplicates 
                pred.next =  head.next
            #otherwise move predecssor
            else:
                pred = pred.next

            #move forward
            head = head.next
        
        return sentinel.next

    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)
