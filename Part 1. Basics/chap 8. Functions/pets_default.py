# positional argumentq

def describe(pet_name, animal_type='fox'):
    """display information about a pet"""
    print(f" \nI have a {animal_type}")
    print(f"My {animal_type}'s pet name is {pet_name.title()}")

describe(pet_name='mash')