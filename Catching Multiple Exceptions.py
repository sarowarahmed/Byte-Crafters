#Write a function that takes two inputs from the user, converts them to integers, and returns their sum. Handle the cases where the inputs cannot be converted to integers and where either input is missing.

def sum_inputs():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a + b
    except ValueError:
        return "Error: Invalid input. Please enter integers."
    except Exception as e:
        return f"Error: {e}"
