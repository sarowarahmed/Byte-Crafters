#Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it
#Eg if the num = 5, den = 15 the answer should be ⅓
#Eg if the num = 6, den = 9 the answer should be ⅔

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

common_divisor = gcd(numerator, denominator)

simplified_numerator = numerator // common_divisor
simplified_denominator = denominator // common_divisor

print(f"Simplified fraction: {simplified_numerator}/{simplified_denominator}")
