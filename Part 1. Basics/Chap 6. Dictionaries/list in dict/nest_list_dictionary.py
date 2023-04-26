"""
You can nest a list inside a dictionary any time you want more than
one value to be associated with a single key in a dictionary
"""

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    # loop over the items to get the values
    for language in language:
        print(f"\t{language.title()}")

# -- output --

# Jen's favorite languages are:
#         Python
#         Ruby

# Sarah's favorite languages are:
#         C

# Edward's favorite languages are:
#         Ruby
#         Go

# Phil's favorite languages are:
#         Python
#         Haskell