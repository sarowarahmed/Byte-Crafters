#Count the frequency of a particular character in a provided string. Eg 'hello how are you' is the string, the frequency of h in this string is 2.

string = input("Enter a string: ")
char = input("Enter a character to find its frequency: ")

frequency = 0
for c in string:
    if c == char:
        frequency += 1

print(f"Frequency of '{char}' in the string is {frequency}")
