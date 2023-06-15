
filename = 'Part 1. Basics\Chap 10. Files and Exceptions\pi_string.txt'

with open(filename, 'w') as file_object:
    file_object.write('i love this course. It has gven me sound background in python')

with open(filename) as file_object:
    lines = file_object.readline()
    print(lines)

