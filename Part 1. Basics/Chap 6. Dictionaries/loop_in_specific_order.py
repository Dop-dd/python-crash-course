"""
Starting in Python 3.7, looping through a dictionary returns the items in
the same order they were inserted. Sometimes, though, you’ll want to loop
through a dictionary in a different order.
One way to do this is to sort the keys as they’re returned in the for loop.
You can use the sorted() function to get a copy of the keys in order:
"""
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

# sorted
for name  in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking then poll. ")

# Edward, thank you for taking then poll.
# Jen, thank you for taking then poll.
# Phil, thank you for taking then poll.
# Sarah, thank you for taking then poll.

# not sorted
for name  in favorite_languages.keys():
    print(f"{name.title()}, thank you for taking then poll. ")

# Jen, thank you for taking then poll.
# Sarah, thank you for taking then poll.
# Edward, thank you for taking then poll.
# Phil, thank you for taking then poll.
