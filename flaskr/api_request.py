import requests
import json
import geocoder
from flask import redirect, request
import time

google_key = 'AIzaSyDc3GdOMZnLnRGztSGHRe9FGATaMEfrSO0'
owm_key = 'c1a0b5df07dfd6f81425799dbbd1c044'

def unix_daily():
    current_day = int(time.time())
    all_days = []
    for n in range(1, 8):
        all_days.append(current_day)
        current_day += 86400
    return all_days

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
    city_state = city + ',' + state + ',US'
    coordinates = get_coordinates(city, state)
    params = {'lat': coordinates[0], 'lon': coordinates[1], 'units': 'imperial', 'exclude': 'current,minutely', 'appid': owm_key }
    base_url = 'https://api.openweathermap.org/data/2.5/onecall?'
    r = requests.get(base_url, params=params)
    dict = r.json()
    daily_weather = {}
    num = 0
    for day in dict['daily']:
        daily_weather[num] = {}
        daily_weather[num]['temp_high'] = str(round(day['temp']['max']))
        daily_weather[num]['temp_low'] = str(round(day['temp']['min']))
        daily_weather[num]['precipitation'] = str(int(day['pop'] * 100)) + '%'
        daily_weather[num]['condition'] = str(day['weather'][0]['main'])
        num += 1
    num = 0
    hourly_weather = {}
    for hour in dict['hourly']:
        hourly_weather[num] = {}
        hourly_weather[num]['temp'] = str(round(hour['temp']))
        hourly_weather[num]['precipitation'] = str(int(hour['pop'] * 100)) + '%'
        hourly_weather[num]['wind_speed'] = str(round(hour['wind_speed'])) + 'mph'
        hourly_weather[num]['condition'] = str(hour['weather'][0]['main'])
        num += 1
    return hourly_weather, daily_weather

def get_current_weather(city, state):
    city_state = city + ',' + state + ',US'
    params = {'q': city_state, 'units': 'imperial', 'appid': owm_key }
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    r = requests.get(base_url, params=params)
    dict = r.json()
    current_weather = {}
    current_weather['temp'] = str(round(dict['main']['temp']))
    current_weather['feels_like'] = str(round(dict['main']['feels_like']))
    current_weather['high'] = str(round(dict['main']['temp_max']))
    current_weather['low'] = str(round(dict['main']['temp_min']))
    current_weather['humidity'] = str(round(dict['main']['humidity'])) + '%'
    current_weather['wind'] = str(round(dict['wind']['speed'])) + 'mph'
    current_weather['condition'] = dict['weather'][0]['description']
    return current_weather
