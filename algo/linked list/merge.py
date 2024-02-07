from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution : 
    def mergeTwoLinkedList(list1:Optional[ListNode],list2 : Optional[ListNode])->Optional[ListNode]:
        new_head =  ListNode(0)
        dummy_new_head = new_head #to keep track of the merged list

        while list1 is not None and list2 is not None :
            if list1.val < list2.val :
                dummy_new_head.next = list1
                list1 = list1.next
            else:
                dummy_new_head.next = list2
                list2 = list2.next
            dummy_new_head = dummy_new_head.next
        
        #now add remaininig of list1/list2 to dummy_new_head
        dummy_new_head.next = list1 if list1 is not None else list2

        return new_head.next

    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 =  ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    mergeTwoLinkedList(list1, list2)

