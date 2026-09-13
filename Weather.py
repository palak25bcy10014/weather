import tkinter as tk
import requests

API_KEY = "AIzaSyDW7VcI3AOgLFpjSP1XjYPfsHgjhzeMf7E"

def get_weather():
    city = city_entry.get().strip()

    try:

        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1}
        ).json()

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        data = requests.get(
            "https://weather.googleapis.com/v1/currentConditions:lookup",
            params={
                "key": API_KEY,
                "location.latitude": lat,
                "location.longitude": lon
            }
        ).json()

        temp = data["temperature"]["degrees"]
        humidity = data["relativeHumidity"]
        condition = data["weatherCondition"]["description"]["text"]

        result.config(
            text=f"{city.title()}\n\n"
                 f"Temperature: {temp}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Weather: {condition}"
        )

    except:
        result.config(text="City not found or API error")

root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")

tk.Label(root, text="Weather App", font=("Times New Roman", 20)).pack(pady=20)

city_entry = tk.Entry(root, font=("Times New Roman", 14))
city_entry.pack(pady=10)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result = tk.Label(root, font=("Times New Roman", 13))
result.pack(pady=20)

root.mainloop()