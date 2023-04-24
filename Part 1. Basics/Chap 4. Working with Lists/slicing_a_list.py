players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#['charles', 'martina', 'michael']

print(players[1:4])
# ['martina', 'michael', 'florence']

""" If you omit the first index in a slice, Python automatically starts your
slice at the beginning of the lis
"""
print(players[:4])
# ['charles', 'martina', 'michael', 'florence']

print(players[2:])
# ['michael', 'florence', 'eli']

print(players[-3:])
# ['michael', 'florence', 'eli']

""" Looping Through a Slice """

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# print("Here are the first three players on my team:")
# Charles
# Martina
# Michael

""" Copying a List """

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

""" Append """
my_foods.append('cannoli')
friends_food.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_food)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'ice cream']