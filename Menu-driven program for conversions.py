#Write a menu driven program - 1. cm to ft  2. KM to Miles  3. USD to INR  4. Exit

while True:
    print("Menu:")
    print("1. Convert cm to ft")
    print("2. Convert KM to Miles")
    print("3. Convert USD to INR")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        cm = float(input("Enter length in centimeters: "))
        feet = cm / 30.48
        print("Length in feet:", feet)
    elif choice == '2':
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print("Distance in miles:", miles)
    elif choice == '3':
        usd = float(input("Enter amount in USD: "))
        inr = usd * 73.5  # Assuming 1 USD = 73.5 INR
        print("Amount in INR:", inr)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
