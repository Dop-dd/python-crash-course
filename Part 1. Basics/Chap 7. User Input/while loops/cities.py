prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"i'd love to go to {city.title()}!")