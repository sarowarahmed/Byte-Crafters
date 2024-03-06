#Write a program that can multiply 2 numbers provided by the user without using the * operator

def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += abs(a)
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        result = -result
    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Result of multiplication:", multiply(num1, num2))
