import requests
import json

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&limit=1&appid=f4f0e831c1fe6b7fef7def5fc6e17422"
    try:
        response = requests.get(url)
        main_temp = response.json().get("main")
        # print(data)
        temperature = round(main_temp["temp"] - 273.15)
        coords = response.json().get("coord")
        lon = coords["lon"]
        lat = coords["lat"]
        return temperature, lon, lat
    except Exception as e:
        print(e)
        get_weather(city)

def keep_going():
    answer = input("Another city ? (y/n)").lower()
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
        temperature, lon, lat = get_weather(city)
        print(f"{city} has {temperature} degrees and is at lon : {lon} and lat : {lat}")
        if keep_going():
            continue
        else:
            break

print("***********")
print("Welcome to the the Weather APP")
print("Please enter a city of which you'd like to know the current weather")
print("***********")

main()
