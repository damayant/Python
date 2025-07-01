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
    # print(calculate(s="(1+(4+5+2))"))





from typing import List

def evaluate_expression(expression: str) -> int:
    """
    Main function to evaluate a mathematical expression containing
    integers, '+', '-', and nested parentheses.
    
    :param expression: A string like "1 + (2 - (3 + 4))"
    :return: Integer result of evaluated expression
    """
    # Remove spaces and convert to list of characters for easier processing
    tokens = list(expression.replace(" ", ""))
    return _evaluate(tokens)

def _evaluate(tokens: List[str]) -> int:
    """
    Recursively evaluates the tokens representing a sub-expression.
    
    :param tokens: List of characters representing the expression.
    :return: Evaluated integer result of the current sub-expression.
    """
    result = 0              # Final result for current sub-expression
    current_number = 0      # Number being currently formed (handles multi-digit)
    current_sign = 1        # Current sign (+1 for '+', -1 for '-')

    while tokens:
        char = tokens.pop(0)  # Get the next character

        if char.isdigit():
            # Build the number by appending digit (supports multi-digit)
            current_number = current_number * 10 + int(char)

        elif char in '+-':
            # Apply the previously built number with its sign
            result += current_sign * current_number
            # Update the sign for the next number
            current_sign = 1 if char == '+' else -1
            # Reset the current number for the next digit(s)
            current_number = 0

        elif char == '(':
            # Start a new sub-expression. Recursively evaluate the part inside ()
            sub_result = _evaluate(tokens)
            # Apply the result of the sub-expression with the current sign
            result += current_sign * sub_result
            current_number = 0  # Reset number after closing bracket

        elif char == ')':
            # On encountering a closing parenthesis, finalize and return current result
            result += current_sign * current_number
            return result

    # Add any number left after the loop ends (when no more tokens)
    return result + current_sign * current_number


# Example usage:
if __name__ == "__main__":
    expression = "1 - (2 + 3 - (4 - 5))"
    print(evaluate_expression(expression))  # Output: -4
    # expression = "(1+(4+5+2)-3)+(6+8)"
    # print(evaluate_expression(expression))  # Output: 23
    # expression = "2-(5-6)"
    # print(evaluate_expression(expression))  # Output: 3