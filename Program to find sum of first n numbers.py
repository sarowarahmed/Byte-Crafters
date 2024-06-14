#Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

n = int(input("Enter a positive integer n: "))

sum_of_numbers = (n * (n + 1)) // 2

print("Sum of first", n, "numbers:", sum_of_numbers)
