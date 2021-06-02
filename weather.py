#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import requests
from datetime import datetime

# getting the weather provider api key from the environment
api_key = os.getenv("OWM_API_KEY")
if not api_key:
    print("no OWM_API_KEY provided")
    sys.exit(1)

# storing the weather provider url in a variable
url = f"http://api.openweathermap.org/data/2.5/weather?id=520555&appid={api_key}"

# testing the connectivity with the weather provider
res = requests.get(url)
if res.status_code != 200:
    print(f"error talking to weather provider: {res.status_code}")
    sys.exit(1)

# getting the main json object
out = res.json()

# printing the city name
city = out['name']    
print(f"Here is the weather report for the city of {city}:")

# printing the temperature
temp = out['main']['temp']
temp_c = temp-273.15
print(f"Temperature is {round(temp_c, 1)} degrees Celsius")

# printing the humidity
humidity = out['main']['humidity']
print(f"Humidity is {humidity}%")

# printing the wind strenght
wind = out['wind']['speed']
print(f"Wind is {round(wind*3.6, 1)} km/h")

# printing the wind kind
if wind < 5.5:
    print("Wind is light")
elif wind >= 5.5 and wind < 10.8:
    print("Wind is moderate")
elif wind >= 10.8:
    print("Wind is strong")

# printing the cloudiness
clouds = out['clouds']['all']
print(f"Cloudiness is {clouds}%")

# printing the sunrise time
rise_stamp = out['sys']['sunrise']
rise_dt = datetime.fromtimestamp(rise_stamp)
rise_str_h = rise_dt.strftime("%H")
rise_str_m = rise_dt.strftime("%M")
rise_h_local = int(rise_str_h)+3
rise_str = str(rise_h_local)+":"+rise_str_m
print(f"Sunrise time is {rise_str} MSK")

# printing the sunset time
sset_stamp = out['sys']['sunset']
sset_dt = datetime.fromtimestamp(sset_stamp)
sset_str_h = sset_dt.strftime("%H")
sset_str_m = sset_dt.strftime("%M")
sset_h_local = int(sset_str_h)+3
sset_str = str(sset_h_local)+":"+sset_str_m
print(f"Sunset time is {sset_str} MSK")

