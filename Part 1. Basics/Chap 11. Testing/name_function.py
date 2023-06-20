"""
Here’s a simple function that takes in a first and last name and
returns a neatly formatted full name
The function get_formatted_name() combines the first and last name
with a space in between to complete a full name, and then capitalizes and
returns the full name. To check that get_formatted_name() works, let’s make
a program that uses this function.
"""

# def get_formatted_name(first, middle, last):
#     full_name = f"{first}  {last}"
#     return full_name.title()

""" making the test to require an optional middle name"""

def get_formatted_name(first, last, middle=''):
        #Generate a neatly formatted full name.
        if middle:
                full_name = f"{first} {middle} {last}"
        else:
               full_name = f"{first} {last}"

        return full_name.title()