filename = 'Part 1. Basics\Chap 10. Files and Exceptions\pi_digit.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:22]}...")
print(len(pi_string))