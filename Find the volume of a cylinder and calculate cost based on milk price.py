#Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

import math
radius = float(input("Enter radius of the cylinder: "))
height = float(input("Enter height of the cylinder: "))

volume = math.pi * radius**2 * height
print("Volume of the cylinder:", volume)

milk_price = 40  # cost of 1 liter milk
total_cost = volume * milk_price
print("Total cost:", total_cost, "Rs")
