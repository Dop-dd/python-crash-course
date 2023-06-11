class Car:

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"this car has {self.odometer_reading} miles on it")


    def update_odometer(self, mileage):

        # Reject the change if it attempts to roll the odometer back.

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Warning! you cannot roll back the mileage')


    # increment through a method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
        self.battery_drive_time_in_hours = 12

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"this can go about {range} miles on full charge")

    def describe_battery(self):
        # print statement describing he battery size
        print(f"this car has a {self.battery_size}-kWh battery")
        print(f"Maximum driving time is {self.battery_drive_time_in_hours} hrs before a recharge")



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        # initialize attribute of the parent class
        super().__init__(make, model, year)

        self.battery = Battery()
        self.driver_mode = "'AUTO'"
        self.number_of_sensors = 45

    # def describe_battery(self):
    #     # print statement describing he battery size
    #     print(f"this car has a {self.battery_size}-kWh battery")
    #     print(f"Maximum diving time is {self.battery_drive_time_in_hours}hrs before a recharge")

    def describe_sensors(self):
        print(f"This car has {self.number_of_sensors} sensors and supports {self.driver_mode} driver mode")
