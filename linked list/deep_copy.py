from typing import Optional


class Node:
    def __init__(self, val=0, next=None, random =  None):
        self.val = val
        self.next = next
        self.random = random

class Solution :
    def copyRandomList(head:Optional[Node])->Optional[Node]:
        current =  head 
        old_to_new = { None : None} #initialising the hashmap for old -> new node

        #this loop is to just create the hashmap of new nodes w/o any linakages
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head 

        #this loop is to create the linkages for the new_node copy
        while current:
            new_node = old_to_new[current]
            new_node.next  =  old_to_new[current.next]
            new_node.random =  old_to_new[current.random]
            current = current.next
        
        return old_to_new[head]