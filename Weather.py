import tkinter as tk
import requests

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
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,weather_code"
            }
        ).json()

        temp = data["current"]["temperature_2m"]
        humidity = data["current"]["relative_humidity_2m"]
        code = data["current"]["weather_code"]

        weather_codes = {
            0: "Clear Sky",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Cloudy",
            45: "Fog",
            51: "Drizzle",
            61: "Rain",
            71: "Snow",
            95: "Thunderstorm"
        }

        weather = weather_codes.get(code, "Weather Condition")

        result.config(
            text=f"{city.title()}\n\n"
                 f"Temperature: {temp}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Weather: {weather}"
        )

    except:
        result.config(text="City not found or API error")


root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")

tk.Label(
    root,
    text="Weather App",
    font=("Times New Roman", 20, "bold")
).pack(pady=20)

city_entry = tk.Entry(
    root,
    font=("Times New Roman", 14)
)
city_entry.pack(pady=10)

tk.Button(
    root,
    text="Get Weather",
    font=("Times New Roman", 12),
    command=get_weather
).pack(pady=10)

result = tk.Label(
    root,
    font=("Times New Roman", 11)
)
result.pack(pady=20)

root.mainloop()
