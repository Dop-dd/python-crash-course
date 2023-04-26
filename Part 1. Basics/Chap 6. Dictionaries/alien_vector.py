"""
For a more interesting example, let’s track the position of an alien that
can move at different speeds. We’ll store a value representing the alien’s
current speed and then use it to determine how far to the right the alien
should move
"""
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien based on it's current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new positon is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position : {alien_0['x_position']}")

# original position: 0
# New position : 2

""" Removing Key-Value Pairs """

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# {'color': 'green', 'points': 5}
# {'color': 'green'}