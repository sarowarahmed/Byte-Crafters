#Define a custom exception NegativeNumberError and write a function that takes a number and raises this exception if the number is negative.

class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative number is not allowed.")
    return number
