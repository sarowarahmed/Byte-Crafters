#Print all factors of a given number provided by the user.

num = int(input("Enter a number: "))
factors = [i for i in range(1, num + 1) if num % i == 0]
print("Factors of", num, "are:", factors)
