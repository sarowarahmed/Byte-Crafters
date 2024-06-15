India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA =["New York", "Chicago", "Las Vegas", "San Francisco"]
England = ["London", "Manchester", "Liverpool", "Nottingham"]

#Write a program that asks users to enter two cities, and it tells you if they both are in the same country or nor />
#For example:
#If I enter Mumbai and Chennai, it will print "Both cities are in India" but if I enter Mumbai and New York it should print "They don't belong to the same country"

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
England = ["London", "Manchester", "Liverpool", "Nottingham"]

# Function to determine if both cities are in the same country
def check_cities(city1, city2):
    if city1 in India and city2 in India:
        return "Both cities are in India"
    elif city1 in USA and city2 in USA:
        return "Both cities are in USA"
    elif city1 in England and city2 in England:
        return "Both cities are in England"
    else:
        return "They do not belong to the same country"

# Taking input from the user
City_1 = input("Enter the first city: ")
City_2 = input("Enter the second city: ")

# Printing the result
print(check_cities(City_1, City_2))
