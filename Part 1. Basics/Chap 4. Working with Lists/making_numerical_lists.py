for value in range(1, 5):
    print(value)

# 1
# 2
# 3
# 4

""" Using range() to Make a List of Numbers"""

"""
If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function. When you wrap list() around a
call to the range() function, the output will be a list of numbers
"""
numbers  = list(range(1, 6))
print(numbers)
# [1, 2, 3, 4, 5]

""" We can also use the range() function to tell Python to skip numbers in a given range """
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# In this example, the range() function starts with the value 2 and then
# adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end
# value, 11,
# [2, 4, 6, 8, 10]

""" Create new number sets """
""" You can create almost any set of numbers you want to using the range()
function. For example, consider how you might make a list of the first 10
square numbers (that is, the square of each integer from 1 through 10). In
Python, two asterisks (**) represent exponents. Here’s how you might put
the first 10 square numbers into a list: """

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# if we put the print within the loop we get:
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)
#print(squares)

"""
1]
[1, 4]
[1, 4, 9]
[1, 4, 9, 16]
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25, 36]
[1, 4, 9, 16, 25, 36, 49]
[1, 4, 9, 16, 25, 36, 49, 64]
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

"""  more concisely """
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(f"this s the square root of the numbers betwen 1 and 11 \n{squares}")

""" Simple Statistics with a List of Numbers """

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
# 0
# 9
# 45