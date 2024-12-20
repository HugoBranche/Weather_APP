import tkinter as tk
import requests
from tkinter import messagebox

# Function to get weather data
def get_weather():
    city = city_entry.get()
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Create complete URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Send the request to OpenWeatherMap API
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] == "404":
            messagebox.showerror("Error", "City not found.")
        else:
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            humidity = main["humidity"]
            description = weather["description"]
            wind_speed = data["wind"]["speed"]
            
            # Display the weather information
            result_label.config(text=f"Temperature: {temperature}°C\n"
                                    f"Humidity: {humidity}%\n"
                                    f"Description: {description}\n"
                                    f"Wind Speed: {wind_speed} m/s")
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")

# Create the main application window
root = tk.Tk()
root.title("Weather App")

# Create the labels, entry, and button for the GUI
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
