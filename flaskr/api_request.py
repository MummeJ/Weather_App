import requests
import geocoder
from flask import redirect

google_key = 'AIzaSyDc3GdOMZnLnRGztSGHRe9FGATaMEfrSO0'
owm_key = 'c1a0b5df07dfd6f81425799dbbd1c044'

def k_to_f(k_temp):
    fahrenheit = (k_temp - 273.15) * 9/5 + 32
    return fahrenheit

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.city, g.state
    else:
        return "Unavailable"

def get_coordinates(city, state):
    params = {'key': google_key, 'address': city + ', ' + state}
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    r = requests.get(base_url, params=params)
    dict = r.json()
    if dict['status'] == 'OK':
        geometry = dict['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']
        return lat, lon

def get_future_weather(city, state):
    coordinates = get_coordinates(city, state)
    params = {'lat': coordinates[0], 'lon':coordinates[1], 'units': 'imperial', 'exclude': 'current+minutely', 'appid': owm_key }
    base_url = 'https://api.openweathermap.org/data/2.5/onecall?'
    r = requests.get(base_url, params=params)
    dict = r.json()
    current_temp = str(round(dict['current']['temp']))
    feels_like = str(round(dict['current']['feels_like']))
    temp_high = str(round(dict['current']['pressure']))
    temp_low = str(round(dict['current']['humidity']))
    sky = str(round(dict['current']['humidity']))
    return current_temp, feels_like, temp_high, temp_low, sky

def get_current_weather(city, state):
    city_state = city + ',' + state + ',US'
    params = {'q': city_state, 'units': 'imperial', 'appid': owm_key }
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    r = requests.get(base_url, params=params)
    dict = r.json()
    current_temp = str(round(dict['main']['temp']))
    feels_like = str(round(dict['main']['feels_like']))
    temp_high = str(round(dict['main']['temp_max']))
    temp_low = str(round(dict['main']['temp_min']))
    sky = dict['weather'][0]['description']
    return current_temp, feels_like, temp_high, temp_low, sky
