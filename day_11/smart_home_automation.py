class Device:
    def device_name(self,device_name,connectivity,light_status,brightness,color):
        self.device_name = device_name
        self.connectivity = connectivity
        self.light_status = light_status
        self.brightness = brightness
        self.color = color

class Network:
    def Handles_connectivity(self):
        print("Connecting issues required!..")

class Smartlight(Device,Network):
    def device_name(self):
        self.devicename = input("Enter your Device name:")
        self.connectivity = input("Do you want to connect to WiFi? (yes/no):").lower()
        self.light_status = input("Do you want to turn on the Smart Light? (yes/no):").lower()
        self.brightness = int(input("Set brightness level (0-100):"))
        self.color = input("Choose a color for the light: ")

    def Handles_connectivity(self):
       if self.connectivity == "yes":
            print("\nConnecting to WiFi...\nConnected successfully!")
       else:
            print("Connecting to Wifi isn't Occurred")

    def smart_light_on_off(self):
        if self.light_status == "on":
            print(f"\nTurning ON the Smart Light...,\nStatus: {self.light_status}")
        else:
            print(f"\nTurning {self.light_status} the Smart Light...\nStatus: {self.light_status}")

    def brightness(self):

        print(f"\nSetting brightness to {self.brightness}%\nBrightness: {self.brightness}")

    def change_color(self):

        print(f"\nChanging color to {self.color}\nCurrent Color: {self.color}")

light = Smartlight()
light.device_name()
light.Handles_connectivity()
light.smart_light_on_off()
light.change_color()


