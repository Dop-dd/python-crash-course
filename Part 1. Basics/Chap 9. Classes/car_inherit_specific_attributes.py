
class Car:

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 60

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):

        # Reject the change if it attempts to roll the odometer back.

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Warning! you cannot roll back the mileage')

    # increment through a method
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        # initialize attribute of the parent class
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery_drive_time_in_hours= 12
        self.driver_mode = "'AUTO'"
        self.number_of_sensors = 45

    def describe_battery(self):
        # print statement describing he battery size
        print(f"this car has a {self.battery_size}-kWh battery")
        print(f"Maximum diving time is {self.battery_drive_time_in_hours}hrs before a recharge")

    def describe_sensors(self):
        print(f"This car has {self.number_of_sensors} sensors and supports {self.driver_mode} driver mode")

print('')
print('\n--- Car make, model and year ---')
my_used_car = Car('Renault', 'Megane', 2005)
print(my_used_car.get_descriptive_name())

print('\n--- Update mileage ---')
my_used_car.update_odometer(53_00)
my_used_car.read_odometer()

print('\n--- Increment mileage ---')
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# electric car callback
print('\n--- Electric  Car ---')
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.describe_sensors()

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(80)
# my_new_car.read_odometer()
