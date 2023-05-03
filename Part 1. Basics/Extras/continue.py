"""
Look carefully, the user enters the first number before the program enters the while loop.
The subsequent number is entered when the program is already in the loop.
"""

largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print(f"\n largest number is {largest_number}")
else:
    print("you haven't enterd any number")
print(f" hit counts: {counter}")