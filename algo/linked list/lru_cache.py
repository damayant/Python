class Node:
    def __init__(self,key,value) -> None:
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.cache={}
        self.head=Node(None,None)
        self.tail=Node(None,None)
        self.head.next=self.tail
        self.tail.prev=self.head

    def _add_node_to_end(self,node):
        last_node=self.tail.prev
        node.next = self.tail
        node.prev=last_node
        last_node.next=node
        self.tail.prev=node

    def _remove_node(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def _move_to_end(self,node):
        self._remove_node(node)
        self._add_node_to_end(node)

    def get(self,key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_end(node)
        return node.value
    
    def put(self,key,value):
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self._move_to_end(node)
        else:
            if len(self.cache)>=self.capacity:
                lru_node = self.head.next
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            
            new_node=Node(key,value)
            self._add_node_to_end(new_node)
            self.cache[key]=new_node
