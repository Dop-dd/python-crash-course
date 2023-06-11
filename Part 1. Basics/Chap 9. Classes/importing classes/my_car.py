from car import Car

print('')

my_used_car = Car('Renault', 'Megane', 2005)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(53_00)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

