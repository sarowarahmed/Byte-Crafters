#Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20lakh< _   – 30%)(0-1lakh print k).

salary = float(input("Enter your salary: "))

HRA = 0.1 * salary
DA = 0.05 * salary
PF = 0.03 * salary

tax = 0
if 0 < salary <= 100000:
    tax = 0
elif 100001 <= salary <= 500000:
    tax = 0.1 * salary
elif 500001 <= salary <= 1000000:
    tax = 0.2 * salary
else:
    tax = 0.3 * salary

net_salary = salary - HRA - DA - PF - tax
print("Net Salary after deductions:", net_salary)
