#Print the first 20 numbers of a Fibonacci series.
a, b = 0, 1
for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b
