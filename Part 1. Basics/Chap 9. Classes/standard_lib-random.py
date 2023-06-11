from random import randint, choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\nAll players on the list:")
print('----')
for player in players:
    print(f" - {player.title()}")

first_up = choice(players)
print(f"\nselected player is: ** {first_up.title()} **")