#Write a program that will give you the sum of 3 digits

num = int(input("Enter a 3-digit number: "))
sum_of_digits = sum(int(digit) for digit in str(num))
print("Sum of digits:", sum_of_digits)
