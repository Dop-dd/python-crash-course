
def word_count_new(filename):

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"please the file {filename} cannot be found")

    else:
        word_count = contents.split()
        number_of_words = len(word_count)

        # calculate total number of letters in the file
        spaces = contents.count(' ')
        letters_count = len(contents)
        num_of_letters = number_of_words - spaces

        #print(f"\n----Displaying the full text----\n {filename} :\n- {word_count} words.")
        print(f"\nThe file {filename} has the follwing atttributes:\n- {number_of_words} words.")
        print(f"- {letters_count} letters including white spaces.")
        print(f"- {num_of_letters} letters with NO white spaces.")


filenames = [
                'Part 1. Basics\Chap 10. Files and Exceptions/alice.txt',
                'Part 1. Basics\Chap 10. Files and Exceptions\siddhartha.txt',
                'Part 1. Basics\Chap 10. Files and Exceptions\moby_dick.txt',
                'Part 1. Basics\Chap 10. Files and Exceptions\little_women.txt'
             ]

for filename in filenames:
    word_count_new(filename)

