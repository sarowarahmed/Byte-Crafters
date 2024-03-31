#Write a python program to remove all the duplicates from a list.

input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)

print("List after removing duplicates:", unique_list)
