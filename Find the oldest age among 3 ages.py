#User will input (3 ages). Find the oldest one


age1 = int(input("Enter age 1: "))
age2 = int(input("Enter age 2: "))
age3 = int(input("Enter age 3: "))

oldest_age = max(age1, age2, age3)
print("The oldest age is:", oldest_age)
