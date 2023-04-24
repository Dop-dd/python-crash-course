requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"sorry we're out of {requested_topping} at the moment")
    else:
        print(f"adding {requested_topping}")
print("\nFinished making your pizza")