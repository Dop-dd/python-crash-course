
phrase = 'the quick brown fox jumps over the lazy dog typing test'
words = phrase.split()
word_count = len(words)

empty_space = phrase.count(' ')
number_of_letters = len(phrase) - empty_space
##letters = len(phrase) - phrase.count(' ')

print(f"\ntotal number of words in the phrase: {word_count}")
print(f"total number of letters , whitespace included: {len(phrase)}")
print(f"total number of letters , No whitespace included: {number_of_letters}")
#print(len(letters))
