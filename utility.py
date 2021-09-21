from googletrans import Translator
import requests
import os

# for more security remove secret key from here and add it to environment variables
WEATHER_SECRET_KEY = os.getenv('WEATHER_SECRET_KEY', '441e6ecae0ed70d5baa3dc11d30a67a7')


async def translate_location(city, country):
    translator = Translator()
    location_in_en = translator.translate(f'{city} {country}', 'en', 'ar').text

    return location_in_en


async def get_location_current_weather(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_SECRET_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = {}
        weather['temperature'] = main['temp']
        weather['humidity'] = main['humidity']
        weather['pressure'] = main['pressure']
        weather['report'] = data['weather']
        return weather

    else:
        print("Error in the HTTP request with weather api")
