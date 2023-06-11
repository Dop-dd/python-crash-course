from car import Car, ElectricCar

my_nissan = Car('nissan', 'sunny', 2009)
print(my_nissan.get_descriptive_name())
my_nissan.update_odometer(53_00)
my_nissan.read_odometer()

my_nissan.increment_odometer(100)
my_nissan.read_odometer()
print()