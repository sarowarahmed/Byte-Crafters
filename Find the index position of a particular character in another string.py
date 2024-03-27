#Find the index position of a particular character in another string. 

string = input("Enter a string: ")
char = input("Enter a character to find its index: ")

index_positions = [index for index, c in enumerate(string) if c == char]

print(f"Index positions of '{char}' in the string are {index_positions}")
