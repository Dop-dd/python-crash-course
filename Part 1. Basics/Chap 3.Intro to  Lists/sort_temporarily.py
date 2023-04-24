# Sorting a List Temporarily with the sorted() Function

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
# Here is the original list:
# ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the sorted list:")
print(sorted(cars))
# Here is the sorted list:
# 'audi', 'bmw', 'subaru', 'toyota']

""" Printing a List in Reverse Order """

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(f"\n{cars}")
print(cars)

#['subaru', 'toyota', 'audi', 'bmw']
# ['subaru', 'toyota', 'audi', 'bmw']

""" Finding the Length of a List """
print(len(cars))
# 4