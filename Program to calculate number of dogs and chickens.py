#Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

total_heads = int(input("Enter total number of heads: "))
total_legs = int(input("Enter total number of legs: "))

# Assuming a dog has 4 legs and a chicken has 2 legs
# Let's solve the system of equations:
# 4 * num_dogs + 2 * num_chickens = total_legs
# num_dogs + num_chickens = total_heads

num_dogs = (total_legs - 2 * total_heads) / 2
num_chickens = total_heads - num_dogs

print("Number of dogs:", num_dogs)
print("Number of chickens:", num_chickens)
