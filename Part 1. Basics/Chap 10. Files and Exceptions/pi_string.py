"""
After you’ve read a file into memory, you can do whatever you want with
that data, so let’s briefly explore the digits of pi. First, we’ll attempt to build
a single string containing all the digits in the file with no whitespace in it:
"""

filename = 'Part 1. Basics\Chap 10. Files and Exceptions\pi_digit.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# ----with strp() -----
# 3.14159265358979323846264338327959793238476643383232
# 52
#----------with r.strip() ------
# 3.1415926535  8979323846  2643383279  5979323847  6643383232
# 60