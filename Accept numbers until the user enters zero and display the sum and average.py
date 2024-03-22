#Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

total = 0
count = 0

while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1

if count == 0:
    print("No numbers were entered.")
else:
    average = total / count
    print("Sum:", total)
    print("Average:", average)
