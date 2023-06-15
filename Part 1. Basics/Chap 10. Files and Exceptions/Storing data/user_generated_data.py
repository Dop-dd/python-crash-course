# remember me
import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it

filename = 'username.json'

username = input('please enter your name: ')


with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"we will remember your when you come back, {username}")

