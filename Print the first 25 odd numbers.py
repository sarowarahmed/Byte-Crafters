#Write a program to print the first 25 odd numbers

count = 0
num = 1
while count < 25:
    if num % 2 != 0:
        print(num, end=" ")
        count += 1
    num += 1
