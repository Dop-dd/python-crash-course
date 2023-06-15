with open('Part 1. Basics\Chap 10. Files and Exceptions\pi_digit.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
