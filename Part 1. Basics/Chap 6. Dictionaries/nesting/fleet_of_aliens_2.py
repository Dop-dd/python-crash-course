"""
In the previous exercise, these aliens all have the same characteristics,
but Python considers each one a separate object, which allows us to modify
 each alien individually.
How might you work with a group of aliens like this? Imagine that one
aspect of a game has some aliens changing color and moving faster as the
game progresses. When it’s time to change colors, we can use a for loop and
an if statement to change the color of aliens. For example, to change the
first three aliens to yellow, medium-speed aliens worth 10 points each, we
could do this:
"""
# Make an empty list for storing aliens.
"""
Because we want to modify the first three aliens, we loop through a
slice that includes only the first three aliens. All of the aliens are green now
but that won’t always be the case, so we write an if statement to make sure
108 Chapter 6
we’re only modifying green aliens. If the alien is green, we change the color
to 'yellow', the speed to 'medium', and the point value to 10, as shown in the
following output:
"""
aliens = []

# # Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

    # change key, values for the first 3 aliens
    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 25
        # elif alien['color'] == 'yellow':
        #     alien['color'] = 'red'
        #     alien['speed'] = 'fast'
        #     alien['points'] = 15

# # Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print('....')

# {'color': 'yellow', 'points': 25, 'speed': 'medium'}
# {'color': 'yellow', 'points': 25, 'speed': 'medium'}
# {'color': 'yellow', 'points': 25, 'speed': 'medium'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# ....

