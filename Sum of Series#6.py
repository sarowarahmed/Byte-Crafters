#Sum of series 1! + 2! + 3! + ... + n!:

import math

n = int(input("Enter the value of n: "))

series_sum = sum(math.factorial(i) for i in range(1, n + 1))
print("Sum of the series:", series_sum)
