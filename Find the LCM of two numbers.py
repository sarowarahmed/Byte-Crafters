#User will provide 2 numbers you have to find the by LCM of those 2 numbers.

def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // hcf(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM of", num1, "and", num2, "is", lcm(num1, num2))
