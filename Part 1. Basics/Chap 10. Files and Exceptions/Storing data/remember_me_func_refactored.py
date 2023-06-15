"""
Let’s refactor greet_user() so it’s not doing so many different tasks.
We’ll start by moving the code for retrieving a stored username to a separate
function:
"""
import json

def get_stored_username():
    """Get stored username if available."""

    filename = 'username.json'

    try:
        with open(filename)as  f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def gree_user():
    """Greet the user by name."""

    username = get_stored_username()

    if username:
        print(f"welcome back {username}")
    else:
        username = input("please enter your username")
        with open(username, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")

gree_user()

