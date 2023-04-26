""" modified code to change key values """

cars = []

for car in range(10):
    new_car = {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
    cars.append(new_car)

# show the first 6 cars
for car in cars[:4]:
    if car['manufacturer'] == 'toyota':
        car['model'] = 'corola'
        car['color'] = 'red'
        #print(car)


# show the first 8 cars
for car in cars[:8]:
    print(car)
print('.....')

# show how many cars have been created
#print(f"total number of vehicles: {len(cars)}")


# {'manufacturer': 'toyota', 'model': 'corola', 'color': 'red'}
# {'manufacturer': 'toyota', 'model': 'corola', 'color': 'red'}
# {'manufacturer': 'toyota', 'model': 'corola', 'color': 'red'}
# {'manufacturer': 'toyota', 'model': 'corola', 'color': 'red'}
# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# .....