#Write a function that takes two integers and divides them, returning the result. Handle the case where the denominator is zero by returning a custom error message.

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
