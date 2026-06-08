import requests
import os

API_KEY = os.getenv("dfef69a8d15225dc27f907b1af518c09")

if not API_KEY:
    # Prompt the user for an API key if the environment variable isn't set.
    API_KEY = input("Enter your OpenWeather API key (or set OPENWEATHER_API_KEY env var): ").strip()
    if not API_KEY:
        print("No API key provided. Set OPENWEATHER_API_KEY or provide a key to continue.")
        exit(1)

city = input("Enter city name: ").strip()

if not city:
    print("Please enter a valid city name.")
    exit()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=10)
    data = response.json()

    if response.status_code == 200:
        print("\n----- Weather Report -----")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
    else:
        print(f"Error: {data.get('message', 'Unable to fetch weather')}")

except requests.exceptions.Timeout:
    print("Error: Request timed out.")
except requests.exceptions.RequestException:
    print("Error: Unable to connect to weather service.")
