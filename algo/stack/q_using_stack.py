class MyQueue:
    
    def __init__(self):
        self.s1 = [] #initialsing the  1st stack
        self.s2 = []  #initialising 2nd stack
        self.tos = 0 #initialising the top of stack element
        

    def push(self, x: int) -> None:
        #if the 1st stack is empty  then initialise tos element to x
        if not self.s1 : 
            self.tos = x
        #add the element to 1st stack
        self.s1.append(x)
        # print("push:",self.s1,self.s2)

    def pop(self) -> int:
        # print("before pop:",self.s1,self.s2)
        #if the 2nd stack is empty then start  popping the 1st stack till its empty and putting into 2nd stack
        if not self.s2 :
            while self.s1:
                self.s2.append(self.s1.pop())
        # print("after pop:",self.s1,self.s2)
        return self.s2.pop()        

    def peek(self) -> int:
        #if the 2nd stack is not empty then pop the 1st element in 2nd stack
        if self.s2:
            return self.s2[-1]
        #if the 2nd stack is empty then return the tos
        return self.tos
        

    def empty(self) -> bool:
        return len(self.s1) == 0  and len(self.s2) == 0 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()