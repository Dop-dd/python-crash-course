cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper().join('**'))
    else:
        print(car.title())

# Audi
# *BMW*
# Subaru
# Toyota
