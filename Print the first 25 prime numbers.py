#Print first 25 prime numbers

count = 0
num = 2
while count < 25:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1
