from typing import List


def evalRPN(tokens:List[str])->int:
    operations = {
        "+": lambda a,b : a+b,
        "-": lambda a,b : a-b,
        "/": lambda a,b : a/b,
        "*": lambda a,b : a*b
    }

    stack = []

    for token in tokens:
        if token in operations:
            number_2 = stack.pop()
            number_1 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_1,number_2))
        else:
            stack.append(int(token))

    return stack.pop()

def evalRPN(tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop()+stack.pop())
            elif tokens[i] == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif tokens[i] == "*":
                stack.append(stack.pop()*stack.pop())
            elif tokens[i] == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else :
                stack.append(int(tokens[i]))
        return stack[0]


print(evalRPN(tokens = ["2","1","+","3","*"]))
