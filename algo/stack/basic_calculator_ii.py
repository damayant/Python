def evaluate_basic_expression(expression: str) -> int:
    """
    Evaluates a basic arithmetic expression string without parentheses,
    containing +, -, *, / with correct operator precedence.

    :param expression: Arithmetic string like "3+2*2"
    :return: Final integer result
    """

    def compute_result_for_previous_operator(
        operator: str, previous_value: int, current_value: int
    ) -> int:
        """
        Applies the arithmetic operation between two values based on the operator.

        Division truncates toward zero (like in Python).
        """
        if operator == '+':
            return current_value
        elif operator == '-':
            return -current_value
        elif operator == '*':
            return previous_value * current_value
        elif operator == '/':
            return int(previous_value / current_value)  # Truncates toward 0
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    def evaluate_tokens(tokens: str) -> int:
        """
        Evaluates the input expression tokens with correct operator precedence using a stack.
        """
        stack = []
        current_number = 0
        previous_operator = '+'  # Initialize to handle the first number

        for index, character in enumerate(tokens):
            if character.isdigit():
                current_number = current_number * 10 + int(character)

            # If we hit an operator or end of string, we evaluate the prior operation
            if character in '+-*/' or index == len(tokens) - 1:
                if previous_operator in '+-':
                    # Push value directly with sign
                    stack.append(
                        compute_result_for_previous_operator(previous_operator, 0, current_number)
                    )
                else:
                    # For * or /, pop and compute with precedence
                    last_value = stack.pop()
                    stack.append(
                        compute_result_for_previous_operator(previous_operator, last_value, current_number)
                    )

                # Reset for next iteration
                previous_operator = character
                current_number = 0

        return sum(stack)

    # Step 1: Clean the input by removing spaces
    cleaned_expression = expression.replace(" ", "")

    # Step 2: Evaluate cleaned expression
    return evaluate_tokens(cleaned_expression)

# Example usage:
if __name__ == "__main__":
    # expression = "3 + 2 * 2"
    # print(evaluate_basic_expression(expression))  # Output: 7

    expression = " 3/2 "
    print(evaluate_basic_expression(expression))  # Output: 1

    # expression = " 3+5 / 2 "
    # print(evaluate_basic_expression(expression))  # Output: 5