#Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

principle = float(input("Enter principle amount: "))
rate_of_interest = float(input("Enter rate of interest: "))
time_period = float(input("Enter time period (in years): "))

simple_interest = (principle * rate_of_interest * time_period) / 100
print("Simple interest:", simple_interest)
