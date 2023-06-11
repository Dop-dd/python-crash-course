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