#Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

if angle1 + angle2 + angle3 == 180:
    print("It can form a triangle.")
else:
    print("It cannot form a triangle.")
