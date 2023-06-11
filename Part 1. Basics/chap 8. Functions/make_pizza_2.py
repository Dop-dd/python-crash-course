def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\n make a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'meaty-mack')
make_pizza(10, '6 chease', 'pepperoni', 'tuna')