"""
When you use the input() function, Python interprets everything the user
enters as a string. We can resolve this issue by using the int() function, which tells
Python to treat the input as a numerical value. The int() function converts
a string representation of a number to a numerical representation,
as shown here:
"""
height = input('enter your height please. ')
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride")
else:
    print("\nYou'l be able to ride when you're a little taller")

# enter your height please. 45

# You'l be able to ride when you're a little taller

# enter your height please. 48

# You're tall enough to ride