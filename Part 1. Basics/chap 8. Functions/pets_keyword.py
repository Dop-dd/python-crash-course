# positional argumentq

def describe(animal_type, pet_name):
    """display information about a pet"""
    print(f" \nI have a {animal_type}")
    print(f"My {animal_type}'s pet name is {pet_name.title()}")

describe(animal_type='rabbit', pet_name='squiggy')