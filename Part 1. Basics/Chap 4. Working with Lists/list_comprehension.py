"""
The approach described earlier for generating the list squares consisted of
using three or four lines of code. A list comprehension allows you to generate
this same list in just one line of code. A list comprehension combines the
for loop and the creation of new elements into one line, and automatically
appends each new element.
"""
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""
begin with a descriptive name for the list, such as
squares. Next, open a set of square brackets and define the expression for
the values you want to store in the new list. In this example the expression
is value**2, which raises the value to the second power. Then, write
a for loop to generate the numbers you want to feed into the expression,
and close the square brackets.
"""