#Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

num = input("Enter a number: ")
num_digits = len(num)
sum_of_powers = sum(int(digit)**num_digits for digit in num)

if int(num) == sum_of_powers:
    print(num, "is a narcissistic number")
else:
    print(num, "is not a narcissistic number")
