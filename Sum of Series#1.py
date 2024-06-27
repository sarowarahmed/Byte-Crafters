#Sum of series 1/1! + 2/2! + ... + n/n!

import math

n = int(input("Enter the value of n: "))

series_sum = sum(i / math.factorial(i) for i in range(1, n + 1))
print("Sum of the series:", series_sum)
