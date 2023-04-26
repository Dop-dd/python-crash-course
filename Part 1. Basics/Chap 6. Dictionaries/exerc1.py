cars = []

for car in range(10):
    new_car = {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
    cars.append(new_car)

# show the first 6 cars
for car in cars[:6]:
    print(car)
print('.....')

# show how many cars have been created
print(f"total number of vehicles: {len(cars)}")

# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# {'manufacturer': 'toyota', 'model': 'suv', 'color': 'black'}
# .....


