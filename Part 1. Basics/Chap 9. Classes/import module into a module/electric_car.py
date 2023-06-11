from car import Car


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
