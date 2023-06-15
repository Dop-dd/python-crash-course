
filename = 'Part 1. Basics\Chap 10. Files and Exceptions\quick_fox.txt'

with open(filename, 'w') as f:
    f.write('the quick brown fox jumps over the lazy dog typing test')

try:
    with open(filename, encoding='utf-8') as f:
         #lines = f.readline() # readlines wraps the result in a list
        #print(lines)

        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file
    #words = contents.split()
    num_of_words = len(contents)
    print(f"the file {filename} has about {num_of_words} words")


#print(lines)

#print(lines.split())