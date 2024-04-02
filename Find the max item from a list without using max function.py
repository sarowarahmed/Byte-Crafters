#Write a python program to find the max item from a list without using the max function.

input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

max_item = input_list[0]
for item in input_list:
    if item > max_item:
        max_item = item

print("Max item in the list is:", max_item)
