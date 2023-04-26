"""
A more realistic example would involve more than three aliens with
code that automatically generates each alien. In the following example we
use range() to create a fleet of 30 aliens:
"""
# Make an empty list for storing aliens.

aliens = []
""" make 30 green aliens using range()"""
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 10, 'speed': 'slow'}
    # append it to aliens list
    aliens.append(new_alien)

    # show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created.
print(f"total number of aliens created: {len(aliens)}")

# output
# {'color': 'green', 'points': 10, 'speed': 'slow'}
# {'color': 'green', 'points': 10, 'speed': 'slow'}
# {'color': 'green', 'points': 10, 'speed': 'slow'}
# {'color': 'green', 'points': 10, 'speed': 'slow'}
# {'color': 'green', 'points': 10, 'speed': 'slow'}
# ...
# total number of aliens created: 30
