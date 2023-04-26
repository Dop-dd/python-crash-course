"""
If you are primarily interested in the values that a dictionary contains,
you can use the values() method to return a list of values without any keys.
For example,
say we simply want a list of all languages chosen in our programming
language poll without the name of the person who chose each
language:
"""

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Python
# C
# Ruby
# Python