#Sum of series 1 + 2x + 3x^2 + ... + nx^(n-1):

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

series_sum = sum(i * x**(i-1) for i in range(1, n + 1))
print("Sum of the series:", series_sum)
