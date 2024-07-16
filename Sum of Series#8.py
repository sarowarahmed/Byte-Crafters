#Sum of series 1 - x + x^2 - x^3 + ... ± x^n:

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

series_sum = sum((-1)**(i-1) * x**i for i in range(1, n + 1))
print("Sum of the series:", series_sum)
