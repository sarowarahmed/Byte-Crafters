#Sum of series 1 + x^2/2 + x^3/3 + ... + x^n/n

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

series_sum = 1 + sum((x ** i) / i for i in range(2, n + 1))
print("Sum of the series:", series_sum)
