"""
The first program will
use json.dump() to store the set of numbers, and the second program will use
json.load().
The json.dump() function takes two arguments: a piece of data to
store and a file object it can use to store the data. Here’s how you can use
json.dump() to store a list of numbers
"""

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)