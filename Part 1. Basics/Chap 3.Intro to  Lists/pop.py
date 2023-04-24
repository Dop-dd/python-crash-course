"""
Removing an Item Using the pop() Method
Sometimes you’ll want to use the value of an item after you remove it from a list.
The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack. In
this analogy, the top of a stack corresponds to the end of a list.
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles)

# ['honda', 'yamaha']

print(popped_motorcycle)
# suzuki - this elemnt was popped out

"""Imagine that the motorcycles
in the list are stored in chronological order according to when we owned
them. If this is the case, we can use the pop() method to print a statement
about the last motorcycle we bought:
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"the last motorcycle Iowed was a {last_owned.title()}")
# the last motorcycle Iowed was a Suzuki