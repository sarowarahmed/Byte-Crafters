#Write a program that can check whether a given string is palindrome or not.

string = input("Enter a string: ")

if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
