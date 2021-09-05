import requests

api_key = 'c1a0b5df07dfd6f81425799dbbd1c044'
input_city = 'Thibodaux'
input_state = 'LA'
input_country = 'US'
city_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(input_city, api_key)
city_state_url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'.format(input_city, input_state, api_key)
city_state_country_url = 'https://api.openweathermap.org/data/2.5/weather?q={},{},{}&appid={}'.format(input_city, input_state, input_country, api_key)

def k_to_f(k_temp):
    fahrenheit = (k_temp - 273.15) * 9/5 + 32
    return fahrenheit

r = requests.get(city_state_country_url)
dict = r.json()
current_temp = round(k_to_f(dict['main']['temp']), 1)
feels_like = round(k_to_f(dict['main']['feels_like']), 1)
temp_high = round(k_to_f(dict['main']['temp_max']), 1)
temp_low = round(k_to_f(dict['main']['temp_min']), 1)
sky = dict['weather'][0]['description']
print('Temperature: ' + str(current_temp))
print('Feels Like: ' + str(feels_like))
print('High: ' + str(temp_high))
print('Low: ' + str(temp_low))
print('Condition: ' + sky)
