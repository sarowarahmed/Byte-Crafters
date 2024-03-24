#Find the length of a given string without using the len() function. 

string = input("Enter a string: ")
length = 0

for char in string:
    length += 1

print("Length of the string:", length)
