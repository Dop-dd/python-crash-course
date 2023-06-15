filename = 'Part 1. Basics\Chap 10. Files and Exceptions\pi_digit.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("enter yorr birthsat,in the form mmddyy: ")
if birthday in pi_string:
    print("your birthday apperas in the first million digits of pi!")

else:
    print("Your birthday does not appear in the first million digits of pi!")
print(birthday)