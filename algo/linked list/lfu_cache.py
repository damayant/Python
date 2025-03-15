from collections import defaultdict

class Node:
    """
    A class representing a node in the doubly linked list.
    Each node stores:
    - key, value
    - frequency count
    - pointers to previous and next nodes
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1  # Frequency count starts at 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """
    A class representing a doubly linked list.
    Used to store nodes with the same frequency count.
    Supports adding nodes to the end (most recently used) and removing the least recently used node.
    """
    def __init__(self):
        self.head = Node(None, None)  # Dummy head
        self.tail = Node(None, None)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add_node(self, node):
        """Adds a node to the end of the list (most recently used)."""
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
    
    def remove_node(self, node):
        """Removes a given node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def pop_head(self):
        """Removes and returns the least recently used node (first node after head)."""
        if self.size > 0:
            node = self.head.next
            self.remove_node(node)
            return node
        return None

class LFUCache:
    """
    A Least Frequently Used (LFU) cache implementation using:
    - A dictionary to store key-node mappings.
    - A dictionary mapping frequency counts to linked lists of nodes.
    - A min_freq tracker to quickly find the least frequently used node.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0  # Tracks the minimum frequency in the cache
        self.node_map = {}  # Stores key -> node mappings
        self.freq_map = defaultdict(DoublyLinkedList)  # Maps frequency -> DLL of nodes
    
    def _update_node(self, node):
        """
        Updates the frequency of a node:
        - Removes it from its current frequency list.
        - Increments its frequency count.
        - Moves it to the new frequency list at the end.
        """
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        
        # If this was the last node in the min_freq list, update min_freq
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
        
        # Increase frequency and move node to new frequency list at the end
        node.freq += 1
        self.freq_map[node.freq].add_node(node)
    
    def get(self, key: int) -> int:
        """Retrieves the value of a key and updates its frequency. Returns -1 if key not found."""
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._update_node(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """Inserts or updates a key-value pair in the cache."""
        if self.capacity == 0:
            return
        
        if key in self.node_map:
            # If key exists, update value and frequency
            node = self.node_map[key]
            node.value = value
            self._update_node(node)
        else:
            # If at capacity, remove the least frequently used node
            if len(self.node_map) >= self.capacity:
                removed_node = self.freq_map[self.min_freq].pop_head()
                if removed_node:
                    del self.node_map[removed_node.key]
            
            # Create a new node and add it to frequency list 1 at the end
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.freq_map[1].add_node(new_node)
            self.min_freq = 1  # Reset min_freq to 1 since we added a new node
