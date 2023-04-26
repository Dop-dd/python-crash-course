alien_0 = {}

alien_0['color'] = 'red'
alien_0['points'] = 5

print(alien_0)

# 'color': 'red', 'points': 5}

""" Modifying Values in a Dictionary """

# To modify a value in a dictionary, give the name of the dictionary with the
# key in square brackets and then the new value you want associated with
# that key. For example, consider an alien that changes from green to yellow
# as a game progresses:

alien_0 = {'color': 'green'}
print(f'the alien is {alien_0["color"]}')

alien_0['color'] = 'yellow'
print(f"the alien is now {alien_0['color']}")

# the alien is green
# the alien is now yellow
