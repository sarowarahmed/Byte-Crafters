#Write a function that attempts to execute another function that might fail. Implement a retry mechanism that retries the function up to three times before giving up and raising an exception.

import random

def unreliable_function():
    if random.choice([True, False]):
        raise ValueError("Random failure occurred")
    return "Success!"

def retry_function(func, retries=3):
    attempts = 0
    while attempts < retries:
        try:
            return func()
        except Exception as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")
            if attempts == retries:
                raise

try:
    result = retry_function(unreliable_function)
    print(result)
except Exception as e:
    print(f"Function failed after retries: {e}")
