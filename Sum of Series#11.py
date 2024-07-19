#Sum of series 1^3 + 2^3 + 3^3 + ... + n^3:

n = int(input("Enter the value of n: "))

series_sum = sum(i**3 for i in range(1, n + 1))
print("Sum of the series:", series_sum)
