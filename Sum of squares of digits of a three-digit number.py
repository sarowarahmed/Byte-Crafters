#Write a program that will take three digits from the user and add the square of each digit.

num = int(input("Enter a three-digit number: "))
sum_of_squares = sum(int(digit)**2 for digit in str(num))
print("Sum of squares of digits:", sum_of_squares)
