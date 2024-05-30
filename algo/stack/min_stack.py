class MinStack:
    def __init__(self):
        self.stack = []
        #to keep track of the min element in the stack
        self.minStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        #check which element is least then add the least element 
        #might happen that the least element already exists and you are adding again
        #to keep the least element corresponding to the element in stack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        #safe to delete the corresponding element  in minstack as
        #for each element in stack we do have the least element in minstack
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
