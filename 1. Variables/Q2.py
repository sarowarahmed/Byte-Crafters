#Can you explain how variable scoping works in Python? What happens in the following code snippet?
x = 10

def outer():
    x = 20
    
    def inner():
        nonlocal x
        x = 30
        print("Inner:", x)
    
    inner()
    print("Outer:", x)

outer()
print("Global:", x)

#Follow-Up:

#What will be printed by this code and why?
#What is the difference between 'global' and 'nonlocal' keywords in Python?
#How would changing 'nonlocal' to 'global' in the 'inner'() function affect the output?