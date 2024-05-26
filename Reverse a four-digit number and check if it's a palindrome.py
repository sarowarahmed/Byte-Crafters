#Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

num = int(input("Enter a four-digit number: "))
reverse_num = int(str(num)[::-1])
print("Reverse:", reverse_num)
if num == reverse_num:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
