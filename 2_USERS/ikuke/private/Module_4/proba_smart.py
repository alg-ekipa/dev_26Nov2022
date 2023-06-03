import random
import tkinter as tk
from PIL import Image, ImageTk

class WeatherStation:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.weather_condition = ""

    def get_weather_data(self):
        # Simulating weather data from the weather station
        self.temperature = random.uniform(-10, 30)  # Random temperature between -10 and 30 degrees Celsius
        self.humidity = random.randint(0, 100)  # Random humidity between 0 and 100 percent
        self.weather_condition = random.choice(["sun", "clouds", "rain"])  # Random weather condition


class SmartHomeAppGUI:
    def __init__(self, root):
        self.inside_temperature = 20
        self.inside_humidity = 50
        self.weather_station = WeatherStation()

        self.root = root
        self.root.title("Smart Home App")

        self.temperature_label = tk.Label(root, text="Inside Temperature: {}°C".format(self.inside_temperature))
        self.temperature_label.pack()

        self.humidity_label = tk.Label(root, text="Inside Humidity: {}%".format(self.inside_humidity))
        self.humidity_label.pack()

        self.weather_icon_label = tk.Label(root)
        self.weather_icon_label.pack()

        self.outside_temperature_label = tk.Label(root, text="Outside Temperature: ")
        self.outside_temperature_label.pack()

        self.outside_humidity_label = tk.Label(root, text="Outside Humidity: ")
        self.outside_humidity_label.pack()

        self.clothing_suggestion_label = tk.Label(root, text="")
        self.clothing_suggestion_label.pack()

        self.update_button = tk.Button(root, text="Update", command=self.update_weather_data)
        self.update_button.pack()

        # Load weather icon images
        self.weather_icon_images = {
            "sun": ImageTk.PhotoImage(Image.open("sun.png")),
            "clouds": ImageTk.PhotoImage(Image.open("clouds.png")),
            "rain": ImageTk.PhotoImage(Image.open("rain.png"))
        }

    def update_weather_data(self):
        self.weather_station.get_weather_data()
        self.display_weather()
        self.display_clothing_suggestion()

    def display_weather(self):
        outside_temperature_text = "Outside Temperature: {}°C".format(self.weather_station.temperature)
        outside_humidity_text = "Outside Humidity: {}%".format(self.weather_station.humidity)
        self.outside_temperature_label.config(text=outside_temperature_text)
        self.outside_humidity_label.config(text=outside_humidity_text)

        # Display weather icon
        weather_icon_image = self.weather_icon_images.get(self.weather_station.weather_condition)
        if weather_icon_image:
            self.weather_icon_label.config(image=weather_icon_image)
            self.weather_icon_label.image = weather_icon_image

    def display_clothing_suggestion(self):
        outside_temperature = self.weather_station.temperature
        if outside_temperature < 0:
            suggestion = "Wear winter clothes!"
        elif outside_temperature < 10:
            suggestion = "Wear a jacket!"
        else:
            suggestion = "No special clothing suggestion."
        self.clothing_suggestion_label.config(text=suggestion)

# Usage
root = tk.Tk()
app = SmartHomeAppGUI(root)
root.mainloop()
