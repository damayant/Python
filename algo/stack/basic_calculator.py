class Solution:

    # def evaluate_expr(self, stack):
        
    #     # If stack is empty or the expression starts with
    #     # a symbol, then append 0 to the stack.
    #     # i.e. [1, '-', 2, '-'] becomes [1, '-', 2, '-', 0]
    #     if not stack or type(stack[-1]) == str:
    #         stack.append(0)
            
    #     res = stack.pop()

    #     # Evaluate the expression till we get corresponding ')'
    #     while stack and stack[-1] != ')':
    #         sign = stack.pop()
    #         if sign == '+':
    #             res += stack.pop()
    #         else:
    #             res -= stack.pop()
    #     return res       

    # def calculate(self, s: str) -> int:

    #     stack = []
    #     n, operand = 0, 0

    #     for i in range(len(s) - 1, -1, -1):
    #         ch = s[i]

    #         if ch.isdigit():

    #             # Forming the operand - in reverse order.
    #             operand = (10**n * int(ch)) + operand
    #             n += 1

    #         elif ch != " ":
    #             if n:
    #                 # Save the operand on the stack
    #                 # As we encounter some non-digit.
    #                 stack.append(operand)
    #                 n, operand = 0, 0

    #             if ch == '(':         
    #                 res = self.evaluate_expr(stack)
    #                 stack.pop()        

    #                 # Append the evaluated result to the stack.
    #                 # This result could be of a sub-expression within the parenthesis.
    #                 stack.append(res)

    #             # For other non-digits just push onto the stack.
    #             else:
    #                 stack.append(ch)

    #     # Push the last operand to stack, if any.
    #     if n:
    #         stack.append(operand)

    #     # Evaluate any left overs in the stack.
    #     return self.evaluate_expr(stack)

    def calculate(s:str)->int:
        cur = res = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit() :
                cur = cur * 10 + int(char) 
            elif char in ['+','-']:
                res += sign * cur 
                sign = 1 if char == "+" else -1
                cur = 0 
            elif char == "(" :
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0 
            elif char == ")":
                res += sign*cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0
        return res + sign*cur
    print(calculate(s="(1+(4+5+2)-3)+(6+8)"))