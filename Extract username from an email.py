#Extract username from a given email. 
#Eg if the email is nitish24singh@gmail.com then the username should be nitish24singh

email = input("Enter an email: ")
username = email.split('@')[0]
print("Username:", username)
