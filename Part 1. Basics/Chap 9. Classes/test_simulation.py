
class Results:

    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.altitude_value = 24

    def get_sensor_readings(self):
       all_values = f"temp:{self.temperature}°C, Hum:{self.humidity} pres:{self.pressure} "
       return all_values.title()

    # line to add altitude
    def get_altitude(self):
        print(f"The altitude here is {self.altitude_value}m above sea level")

    def update_altitude(self, height):
        #self.altitude_value = height
        if height > self.altitude_value:
            self.altitude_value = height
            print("Sensor is in the Wallon region")

        elif height < self.altitude_value:
            self.altitude_value = height
            print("Sensor is in the Brabant region")

new_values = Results(25, 48, 9)
print(new_values.get_sensor_readings())
new_values.update_altitude(20)
new_values.get_altitude()
