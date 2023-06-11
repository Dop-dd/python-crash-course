# Using a while Loop with Lists and Dictionaries

responses = {}

# et a flag
polling_active = True

while polling_active:
    # prompt for a person's name
    name = input('\nwhat is your name? ')
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the dictionary
    responses[name] = response
    print(response, name)
    print(responses)

    # # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

    # pollong is complete
print('\n --- polling results -----')
for name, response in responses.items():
    print(f"{name} would like to climb {response} someday!")
