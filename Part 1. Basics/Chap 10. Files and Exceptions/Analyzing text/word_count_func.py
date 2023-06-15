
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"sorry the file {filename} does not exist")

    else:
        words = contents.split()
        num_words = len(words)

        # number ofletters
        num_letters = len(filename)
        # empty space
        space = filename.count(' ')
        white_spaces = num_words - space

        print(f"\nThe file {filename} has the follwing atttributes:\n- {num_words} words.")
        print(f"- {num_letters} letters including white spaces.")
        print(f"- {white_spaces} letters with NO white spaces.")


filename = 'Part 1. Basics\Chap 10. Files and Exceptions\quick_fox.txt'
count_words(filename)

