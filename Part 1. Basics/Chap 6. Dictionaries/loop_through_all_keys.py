# Looping Through All the Keys in a Dictionary
"""
The keys() method is useful when you don’t need to work with all of the
values
in a dictionary. Let’s loop through the favorite_languages dictionary
and print the names of everyone who took the poll:"""

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# Jen
# Sarah
# Edward
# Phil


"""
Looping through the keys is actually the default behavior when looping
through a dictionary, so this code would have exactly the same output if you
wrote . . .
"""

