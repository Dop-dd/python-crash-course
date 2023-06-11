"""
Sometimes you’ll want to accept an arbitrary number of arguments, but you
won’t know ahead of time what kind of information will be passed to the
function. One example involves building user
profiles: you know you’ll get information about a user, but you’re not sure
what kind of information you’ll receive. The function build_profile() in the
Functions 149
following example always takes in a first and last name, but it accepts an
arbitrary number of keyword arguments as well
"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('dop', 'donald',
                             location='belgium',
                             profession='developer')

print(user_profile)
