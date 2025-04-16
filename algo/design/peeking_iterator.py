class Iterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def hasNext(self):
        return self.index < len(self.nums)

    def next(self):
        if self.hasNext():
            value = self.nums[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration("No more elements in the iterator")  # Raise an exception if no more elements

class PeekingIterator:
    def __init__(self,iterator):
        self._next=iterator.next() if iterator.hasNext() else None
        self._iterator=iterator

    def peek(self):
        return self._next
    
    def next(self):
        if self._next is None:
            raise StopIteration("No more elements in the iterator")
        current=self._next
        self._next=self._iterator.next() if self._iterator.hasNext() else None  
        return current
    
    def hasNext(self):
        return self._next is not None
    
# Example usage:
nums = [1, 2, 3]
iterator = Iterator(nums)
peeking_iterator = PeekingIterator(iterator)
print(peeking_iterator.peek())  # Output: 1
print(peeking_iterator.next())  # Output: 1
print(peeking_iterator.peek())  # Output: 2
print(peeking_iterator.next())  # Output: 2
print(peeking_iterator.hasNext())  # Output: True
print(peeking_iterator.next())  # Output: 3
print(peeking_iterator.hasNext())  # Output: False
# Output: False
# Note: The above example usage is just for demonstration purposes.
# Time Complexity:O(1) for peek and hasNext, O(1) for next
# Space Complexity:O(1) for storing the next element