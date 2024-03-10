#Print all the armstrong numbers in the range of 100 to 1000

for num in range(100, 1000):
    sum_of_cubes = sum(int(digit)**3 for digit in str(num))
    if num == sum_of_cubes:
        print(num)
