from typing import Optional


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next =  next

class Solution :
    def deleteDuplicatesUsingHashMap(head:Optional[ListNode])->Optional[ListNode]:
        set = {}
        new_head = ListNode(0)
        dummy = new_head
        current = head
        
        while current :
            if current.val in set :
                set[current.val] += 1
            else :
                set[current.val] = 1
            current =  current.next

        current = head
        while current:
            prev= current
            if set[current.val] >1 :
                for i in range(set[current.val]):
                    current = current.next
            else :
                dummy.next = prev
                current = current.next
                dummy = dummy.next 
            
        dummy.next = None
        return new_head.next

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
