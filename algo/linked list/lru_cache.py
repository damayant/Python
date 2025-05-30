class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)  # Dummy head node
        self.tail = Node(None, None)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_to_end(self, node):
        # Add a node to the end of the doubly linked list
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        # Remove a node from the doubly linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_end(self, node):
        # Move a node to the end of the doubly linked list (most recently used)
        self._remove_node(node)
        self._add_node_to_end(node)

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_end(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used item from the linked list and cache
                lru_node = self.head.next
                self._remove_node(lru_node)
                del self.cache[lru_node.key]

            # Add a new node to the linked list and cache
            new_node = Node(key, value)
            self._add_node_to_end(new_node)
            self.cache[key] = new_node


