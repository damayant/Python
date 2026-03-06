import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        # Maps value -> set of indices where it appears in self.list
        self.dict = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        is_new = val not in self.dict or not self.dict[val]
        self.dict[val].add(len(self.list))
        self.list.append(val)
        return is_new

    def remove(self, val: int) -> bool:
        if not self.dict[val]:
            return False
        
        # 1. Get an index of the value to remove and the last element in the list
        idx_to_remove = self.dict[val].pop()
        last_element = self.list[-1]
        last_idx = len(self.list) - 1
        
        # 2. Swap logic: overwrite the element to remove with the last element
        self.list[idx_to_remove] = last_element
        # Update the index of the swapped element in the dictionary
        self.dict[last_element].add(idx_to_remove)
        self.dict[last_element].discard(last_idx)
        
        # 3. Finalize: remove the last element from the list
        self.list.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)