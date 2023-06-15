filename = 'Part 1. Basics\Chap 10. Files and Exceptions\pi_digit.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
