#Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    print("Profit")
elif selling_price < cost_price:
    print("Loss")
else:
    print("No profit, no loss")
