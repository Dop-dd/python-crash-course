"""
A List in a Dictionary
Rather than putting a dictionary inside a list, it’s sometimes useful to put
a list inside a dictionary. For example, consider how you might describe a
pizza that someone is ordering. If you were to use only a list, all you could
really store is a list of the pizza’s toppings. With a dictionary, a list of toppings
can be just one aspect of the pizza you’re describing.
In the following example, two kinds of information are stored for each
pizza: a type of crust and a list of toppings. The list of toppings is a value
associated with the key 'toppings'. To use the items in the list, we give the
name of the dictionary and the key 'toppings', as we would any value in the
dictionary. Instead of returning a single value, we get a list of toppings:
"""
# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'olives']
}
 # Summarize the order.
print(f"you ordered a {pizza['crust']}-crust pizza"
      " with the follwoing toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

""" output """
# you ordered a thick-crust pizza with the follwoing toppings:
#         mushrooms
#         extra cheese
#         olives