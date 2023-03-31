import pyowm
import socket
from pyowm import OWM

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
