"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        oldToNew = {None: None}

        #first loop to just create copy nodes w/o links
        while current :
            oldToNew[current] = Node(current.val)
            current = current.next
        
        current = head
        
        #this loop is to create the linkage of the new copy nodes
        while current :
            new_node = oldToNew[current]
            new_node.next = oldToNew[current.next]
            new_node.random = oldToNew[current.random]
            current = current.next
        
        return oldToNew[head]