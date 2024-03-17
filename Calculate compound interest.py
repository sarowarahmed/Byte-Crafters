#Write a program to find the compound interest.
def compound_interest(principal, rate, time):
    amount = principal * (1 + rate/100)**time
    return amount - principal

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period in years: "))

ci = compound_interest(principal, rate, time)
print("Compound Interest is", ci)
