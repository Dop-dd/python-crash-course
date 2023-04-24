dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 200
# 50

for dimension in dimensions:
    print(dimension)

""" can assign a new value to a variable that represents a tuple. """
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# alter it
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)

# Modified dimensions:
# 400
# 100
