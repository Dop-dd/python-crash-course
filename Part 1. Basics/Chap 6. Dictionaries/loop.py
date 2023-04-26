"""
You can access any single piece of information about user_0 based
on what you’ve already learned in this chapter. But what if you wanted to
see everything stored in this user’s dictionary? To do so, you could loop
through the dictionary using a for loop:
"""

user = {
    'username': 'dopdd',
    'first': 'dop',
    'last': 'donald',
}
# loop through the dict
for key, value in user.items():
    print(f"\nkey: {key}")
    print(f"value, {value}")

# for first, last in user.items():
#     print(f"\nfirst: {first}")
#     print(f"last, {last}")
