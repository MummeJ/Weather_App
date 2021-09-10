import requests
import geocoder
from flask import redirect

api_key = 'c1a0b5df07dfd6f81425799dbbd1c044'

def k_to_f(k_temp):
    fahrenheit = (k_temp - 273.15) * 9/5 + 32
    return fahrenheit

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.city, g.state
    else:
        return "Unavailable"


def get_weather(city, state):
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={},{},US&appid={}'.format(city, state, api_key))
    dict = r.json()
    current_temp = str(round(k_to_f(dict['main']['temp']), 1))
    feels_like = str(round(k_to_f(dict['main']['feels_like']), 1))
    temp_high = str(round(k_to_f(dict['main']['temp_max']), 1))
    temp_low = str(round(k_to_f(dict['main']['temp_min']), 1))
    sky = dict['weather'][0]['description']
    return current_temp, feels_like, temp_high, temp_low, sky
