from pyowm import OWM
import pyowm
import requests


class OpenWeatherMapClient:
    def __init__(self, api_key):
        self.owm_client = OWM(api_key)

    def get_current_weather(self, location):
        # Send a request to the OpenWeatherMap API to get the current weather for the given location
        mgr = self.owm_client.weather_manager()
        # list_of_locations = mgr.locations_for('Tokyo', country='JP', matching='exact')
        # tokyo = list_of_locations[0]
        weather = mgr.weather_at_place(str(location['country'])).get_weather()
        # Return the weather data
        print(weather.weather.detailed_status)
        return weather

    def get_user_location(self):
        # Set up the API URL and request headers
        # Get complete geolocation for the calling machine's IP address
        url = "http://ipwho.is/"
        geolocation = requests.get(url=url)
        geolocation = geolocation.json()
        return {'country': geolocation['country'], 'city': geolocation['city']}
        # return geolocation


weather_client = OpenWeatherMapClient(api_key='c548bc34f606696689b7c67ce8cbdbc7')
weather = weather_client.get_current_weather(weather_client.get_user_location())