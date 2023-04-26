# The get() method requires a key as a first argument. As a second
# optional argument, you can pass the value to be returned if the key doesn’t exist:

alien_0 = {'color': 'green', 'speed': 'slow', 'points': 25}

points_of_value = alien_0.get('direction', 'no direction given')
print(points_of_value)
