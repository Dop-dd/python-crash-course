"""
A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a
dictionary.
In Python, a dictionary is wrapped in braces, {}, with a series of keyvalue
pairs inside the braces,

"""

"""
Consider a game featuring aliens that can have different colors and point
values. This simple dictionary stores information about a particular alien:
"""

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# green
# 5

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"you ve just earned {new_points} points!")

# you ve just earned 5 points!

""" Adding New Key-Value Pairs """

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# {'color': 'green', 'points': 5}
# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
