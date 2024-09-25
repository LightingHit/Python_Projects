# Steps to Follow:
# Set Up an OpenWeatherMap API Account:

# Input: Ask the user to input the city for which they want weather information.
# API Request: Use the city name to make a request to the OpenWeatherMap API and retrieve weather data.
# Output: Display the following weather information:
# Current temperature
# Weather condition (e.g., sunny, cloudy)
# Humidity level
# Forecast for the next few days (optional)
# Make an API Request to Get Weather Data:
#
# The OpenWeatherMap API URL for the current weather is:
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}
# You can pass the city name and your API key as parameters to retrieve weather information.
# The response will be in JSON format, so you'll need to extract the relevant data (like temperature, weather condition, etc.) from the JSON response.
# Handle Units for Temperature:
#
# The API will give you temperature in Kelvin by default. You can convert it to Celsius or Fahrenheit:
# Celsius: C = K - 273.15
# Fahrenheit: F = (K - 273.15) * 9/5 + 32
# Alternatively, you can pass a units parameter to the API call to get temperatures directly in Celsius or Fahrenheit:
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric (for Celsius)
# Handle Errors:
#
# Ensure you handle cases where the user provides an invalid city name.
# Handle connection errors or bad responses from the API gracefully by providing meaningful error messages.
# Full Example Structure:
# Here's a more detailed set of instructions along with a template for how the code might look.
#
# 1. Set Up API and Libraries:
# Import necessary libraries (requests, json).
# Get the city name input from the user.
# 2. Make an API Call:
# Use the requests.get() function to fetch the weather information.
# Parse the JSON response.
# 3. Extract and Display the Data:
# Extract temperature, weather condition, humidity, etc., from the response.
# Display it in a user-friendly way.

import requests
import json

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&limit=1&appid=f4f0e831c1fe6b7fef7def5fc6e17422"
    try:
        response = requests.get(url)
        data = response.json()
        # print(json.dumps(data, indent = 4))
        degrees = data.get("main")
        temp = round(degrees["temp"] - 273.15)
        return temp
    except Exception as e:
        print(e)
        get_weather(city)

def keep_going():
    answer = input("Another city ? (y/n)")
    if not answer.isalpha():
        print("Please enter a valid answer : y or n")
        keep_going()
    else:
        if answer == "y":
            return True
        else:
            return False
def main():
    while True:
        city = input("City : ").capitalize()
        data = get_weather(city)
        print(data)
        if keep_going():
            continue
        else:
            break

print("**********")
print("Welcome to the the Weather APP")
print("Please enter a city of which you'd like to know the current weather")
print("**********")

main()
