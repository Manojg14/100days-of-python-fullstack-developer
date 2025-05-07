
class SpaceObject:

    def __init__(self, object_id, name):
        self.object_id = object_id
        self.name = name

    def show_object_info(self):
        print(f"Object ID: {self.object_id}")
        print(f"Name: {self.name}")


class Satellite(SpaceObject):

    def __init__(self, object_id, name, orbit_type):
        super().__init__(object_id, name)
        self.orbit_type = orbit_type

    def show_satellite_info(self):
        self.show_object_info()
        print(f"Orbit Type: {self.orbit_type}")


class WeatherSatellite(Satellite):

    def __init__(self, object_id, name, orbit_type, sensors):
        super().__init__(object_id, name, orbit_type)
        self.sensors = sensors
        self.active = True

    def show_weather_satellite_info(self):
        self.show_satellite_info()
        print(f"Sensors: {', '.join(self.sensors)}")

    def collect_data(self):
        if self.active:
            print(f"{self.name} collecting data using: {', '.join(self.sensors)}")
        else:
            print(f"{self.name} is deactivated. Cannot collect data.")

    def transmit_data(self):
        if self.active:
            print(f"{self.name} transmitting data to Earth Station...")
        else:
            print(f"{self.name} is deactivated. Cannot transmit data.")

    def check_sensor_health(self):
        print(f"Checking health for sensors on {self.name}...")
        for sensor in self.sensors:
            print(f"{sensor}: OK")

    def add_sensor(self, new_sensor):
        if new_sensor not in self.sensors:
            self.sensors.append(new_sensor)
            print(f"Sensor '{new_sensor}' added.")
        else:
            print(f"Sensor '{new_sensor}' already exists.")

    def log_data(self):
        try:
            with open("satellite_log.txt", "a") as file:
                file.write(f"{self.object_id},{self.name},{self.orbit_type},{','.join(self.sensors)}\n")
            print("Satellite data logged successfully.")
        except Exception as e:
            print(f"Error logging data: {e}")

    def deactivate(self):
        self.active = False
        print(f"{self.name} is now deactivated and no longer transmitting data.")

def get_user_input():
    print("Welcome to the Satellite Tracking System!\n")

    object_id = input("Enter Satellite Object ID: ")
    name = input("Enter Satellite Name: ")
    orbit_type = input("Enter Orbit Type (LEO, MEO, GEO): ")

    sensors_input = input("Enter sensors (Infrared, Thermal, Humidity Sensor): ")
    sensors = [sensor.strip() for sensor in sensors_input.split(",")]

    return WeatherSatellite(object_id, name, orbit_type, sensors)


if __name__ == "__main__":

    satellite = get_user_input()
    satellite.show_weather_satellite_info()

    satellite.collect_data()
    satellite.transmit_data()
    satellite.check_sensor_health()

    new_sensor = input("\nEnter a new sensor to add: ")
    satellite.add_sensor(new_sensor)

    satellite.log_data()
    satellite.deactivate()
    satellite.collect_data()
    satellite.transmit_data()
