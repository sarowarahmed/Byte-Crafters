#User will input (2 Numbers). Write a program to swap the numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1, num2 = num2, num1

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)
