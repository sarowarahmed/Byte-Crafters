#Sum of series 1 - 2 + 3 - 4 + ... ± n:

n = int(input("Enter the value of n: "))

series_sum = sum(i if i % 2 != 0 else -i for i in range(1, n + 1))
print("Sum of the series:", series_sum)
