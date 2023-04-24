cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()

print(cars)
# ['audi', 'bmw', 'subaru', 'toyota']. -  after sorting alphabetically

"""
You can also sort this list in reverse alphabetical order by passing the
argument reverse=True to the sort() method
"""

cars.sort(reverse=True)
print(cars)
