#Sum of series 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!:

import math

n = int(input("Enter the value of n: "))

series_sum = sum(1/math.factorial(i) for i in range(n + 1))
print("Sum of the series:", series_sum)
