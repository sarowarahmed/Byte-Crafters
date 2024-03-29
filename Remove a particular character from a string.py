#Write a program which can remove a particular character from a string. 

string = input("Enter a string: ")
char_to_remove = input("Enter a character to remove: ")

result_string = ''.join(char for char in string if char != char_to_remove)

print("String after removing character:", result_string)
