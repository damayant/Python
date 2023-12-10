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


print(evalRPN(tokens = ["2","1","+","3","*"]))
