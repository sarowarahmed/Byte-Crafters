#Write a function that performs an arithmetic operation (addition, subtraction, multiplication, division) based on a given operator. Raise a custom InvalidOperatorError if the operator is not one of the four basic operations. Use exception chaining to provide additional context if an error occurs.

class InvalidOperatorError(Exception):
    pass

def perform_operation(a, b, operator):
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        else:
            raise InvalidOperatorError(f"Invalid operator: {operator}")
    except Exception as e:
        raise Exception("An error occurred while performing the operation.") from e
