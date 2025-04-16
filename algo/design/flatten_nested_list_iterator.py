class NestedInteger:
    def __init__(self, value):
        self.value = value

    def isInteger(self):
        """Return True if this NestedInteger holds a single integer, rather than a nested list."""
        return isinstance(self.value, int)

    def getInteger(self):
        """Return the single integer that this NestedInteger holds, if it holds a single integer."""
        return self.value

    def getList(self):
        """Return the nested list that this NestedInteger holds, if it holds a nested list."""
        return self.value
    
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._integers=[]
        self._position= -1
        def flatten(nested_list):
            for nest in nested_list:
                if nest.isInteger():
                    self._integers.append(nest.getInteger())
                else:
                    flatten(nest.getList())
        flatten(nestedList)
    
    def next(self) -> int:
        self._position+=1
        return self._integers[self._position]
        
    
    def hasNext(self) -> bool:
        return self._position+1<len(self._integers)

    
# Example usage:
nestedList = [NestedInteger([1, 2]), NestedInteger(3), NestedInteger([4, NestedInteger([5])])]
iterator = NestedIterator(nestedList)
print(iterator.next())  # Output: 1
# print(iterator.hasNext())  # Output: True
# print(iterator.next())  # Output: 2
# print(iterator.hasNext())  # Output: True
# print(iterator.next())  # Output: 3
# print(iterator.hasNext())  # Output: True
# print(iterator.next())  # Output: 4
# print(iterator.hasNext())  # Output: True
# print(iterator.next())  # Output: 5
# print(iterator.hasNext())  # Output: False
#Time Complexity: O(n) for flattening the list, O(1) for next and hasNext
#Space Complexity: O(n) for storing the flattened list

    