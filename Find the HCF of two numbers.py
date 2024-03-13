#User will provide 2 numbers you have to find the HCF of those 2 numbers.

def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("HCF of", num1, "and", num2, "is", hcf(num1, num2))
