responses = {}

review_active = True

while review_active:
    name = input('\nwhat is your name? ')
    response = input('what is the best book you \'ve ever read? ')

    responses[name] = response
    print(responses)

    repeat = input('would you like another person to review a book? (yes/ no) ')
    if repeat == 'no':
       review_active= False

# print results
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f'{name} would like to climb {response}.')