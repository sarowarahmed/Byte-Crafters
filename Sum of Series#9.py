#Sum of series 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/n^2:

n = int(input("Enter the value of n: "))

series_sum = sum(1/i**2 for i in range(1, n + 1))
print("Sum of the series:", series_sum)
