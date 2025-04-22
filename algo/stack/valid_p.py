class Solution (object):
    def isValid(self,expression:str):

        #stack to keep track of opening brackets
        stack = []

        #hashmap to keep track of mappings
        #it makes adding more type os brackets easier
        close_to_opening_map = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        #for every bracket in the expression
        for bracket in expression:
            #if the character is  a closing bracket
            if bracket in close_to_opening_map:
                #Pop the topmost element from the stack, if it is non empty
                #Otherwise assign a dummy value of '#' to the top_element variable
                top_element =  stack.pop() if stack else '#'

                #the mapping for opening bracket in our hash and 
                #the top element of the stack dont match return false
                if close_to_opening_map[bracket] != top_element:
                    return False
            else:
                #we have an opening bracket , simply push it onto the stack
                stack.append(bracket)

            #if the stack is empty at the end , then we have a valid expression . 
        return not stack

#Example usage
if __name__ == "__main__":
    expression = "{[]}"
    sol = Solution()
    print(sol.isValid(expression))  # Output: True
    expression = "{[()}"
    print(sol.isValid(expression))  # Output: False