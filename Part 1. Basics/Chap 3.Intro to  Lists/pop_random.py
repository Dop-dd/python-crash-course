"""
Popping Items from any Position in a List
You can use pop() to remove an item from any position in a list by including
the index of the item you want to remove in parentheses.
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"the first motorcycle i ever owned was a {first_owned.title()}")

# the first motorcycle i ever owned was a Honda

next_owned = motorcycles.pop(1)
print(f"the next motorcycle i bought was a {next_owned.title()}")

# the next motorcycle i bought was a Suzuki

""" Removing an Item by Value """

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} it too expensive for me!")
# A Honda it too expensive for me!
