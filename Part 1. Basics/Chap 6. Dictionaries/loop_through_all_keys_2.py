"""
You can choose to use the keys() method explicitly if it makes your code
easier to read, or you can omit it if you wish.
You can access the value associated with any key you care about inside
the loop by using the current key. Let’s print a message to a couple of friends
about the languages they chose. We’ll loop through the names in the dictionary
as we did previously, but when the name matches one of our friends, we’ll
display a message about their favorite language:
"""
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, i can see that you love {language}")

if 'erin' not in favorite_languages:
    print("\nplease erin take our poll!")


# Jen
# Sarah
#         Sarah, i can see that you love C
# Edward
# Phil
#         Phil, i can see that you love Python

# please erin take our poll!
