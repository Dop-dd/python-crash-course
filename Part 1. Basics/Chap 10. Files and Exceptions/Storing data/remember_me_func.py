
import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:

        username = input('enter you name: ')
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we will remember you next time {username}")
    else:
        print(f"welcome back {username}")

greet_user()



