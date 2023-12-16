class Solution : 
    def evaluate_expression(stack):
        #if stack is empty or starts with a symbol then append 0 to the stack
        #ie [1, '-', 2, '-'] becomes [1, '-', 2, '-', 0]

        if not stack or type(stack[-1]) == str :
            stack.append(0)

        res =  stack.pop()


        #evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(s:str)->int:
        stack =[]
         for i in range(len(s)-1):
             ch = s[i]

             if ch.isdigit() : 
                 operand = 