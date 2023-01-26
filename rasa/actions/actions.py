from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import keyboard
import pyautogui
import webbrowser
import time
import pyowm
import socket
from pyowm import OWM
import requests
from .mic_functions.text_to_sound import read_to_user

class ActionHelloWorld(Action):
    def name(self):
         return "action_hello_world"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Hello World!")
        return []

class Enter(Action):
    def name(self):
        return "action_enter"
    def run(self, dispatcher, tracker, domain):
        keyboard.send("enter")
        dispatcher.utter_message(text="enter pressed")
        read_to_user("enter pressed")


class Escape(Action):
    def name(self):
        return "action_escape"
    def run(self, dispatcher, tracker, domain):
        keyboard.send("escape")
        dispatcher.utter_message(text="enter escape")
        read_to_user("enter escape")


class Space(Action):
    def name(self):
        return "action_space"
    def run(self, dispatcher, tracker, domain):
        keyboard.send("space")
        print("space pressed")
        dispatcher.utter_message(text="space pressed")
        read_to_user("space pressed")


class ArrowDown(Action):
    def name(self):
        return "action_arrow_down"
    def run(self, dispatcher, tracker, domain):
        keyboard.send("arrow_down")
        print("arrow down pressed")
        dispatcher.utter_message(text="arrow down pressed")
        read_to_user("arrow down pressed")

        
class ScrollDown(Action):
    def name(self):
        return "action_scroll_down"
    def run(self, dispatcher, tracker, domain):
        pyautogui.scroll(-100)
        # Send a message to the user
        dispatcher.utter_message(text="arrow down pressed and page scrolled down")
        read_to_user("scroll down pressed")


class OpenYouTube(Action):
    def name(self):
        return "action_open_YT"
    def run(self, dispatcher, tracker, domain):
        user_input = tracker.latest_message.get("text")
        # cutting only the research query
        if 'youtube' in user_input :
            user_input = user_input.split('youtube')[1]
        if  'YouTube' in user_input:
            user_input = user_input.split('YouTube')[1]
        
        # Open YouTube in a new tab
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query={}".format(user_input))

        # Send a message to the user
        dispatcher.utter_message(text="Searching for '{}' on YouTube".format(user_input))
        read_to_user("Searching for '{}' on YouTube".format(user_input))


##################################################################################
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


class GetWeatherAction(Action):
    def __init__(self):
        # Set up the OpenWeatherMap API client
        self.weather_client = OpenWeatherMapClient(api_key='2ae49291af8d453a917666db8d5ab3be')

    def name(self):
        return "action_get_current_weather"

    def run(self, dispatcher, tracker, domain):
        # Get the location from the user's message
        location = self.weather_client.get_user_location()
        dispatcher.utter_message(location)
        print(location)
        location = location['city'] + ", " + location['country']
 
        # Use the OpenWeatherMap API to get the current weather for the location
        weather = self.weather_client.get_current_weather(location)

        # Build a message with the weather information
        message = f"The current weather in {location} is {weather.temperature('celsius')['temp']}°C and {weather.detailed_status}."

        # Check if it is raining and include that information in the message
        if 'rain' in weather.weather:
            message += " It is currently raining."
        else:
            message += " It is not currently raining."

        # Check if it is cloudy and include that information in the message
        if 'clouds' in weather.weather:
            message += " The sky is cloudy."
        else:
            message += " The sky is clear."

        dispatcher.utter_message(text=message)
        read_to_user(message)


class GetTommorowWeatherAction(Action):
    def __init__(self):
        # Set up the OpenWeatherMap API client
        self.weather_client = OpenWeatherMapClient(api_key='2ae49291af8d453a917666db8d5ab3be')
        pass
    
    def name(self):
        return "action_get_tommorow_weather"

    def run(self, dispatcher, tracker, domain):
        # Get the location from the user's message
        location = self.weather_client.get_user_location()
        location = location['city'] + ", " + location['country']

        # Use the OpenWeatherMap API to get the current weather for the location
        weather = self.weather_client.weather_at_place(location).get_weather()

        # Use the OpenWeatherMap API to get the forecast for the location
        forecast = self.weather_client.three_hours_forecast(location)

        # Get the start and end timestamps for the next day
        tomorrow = pyowm.timeutils.tomorrow()
        end_of_tomorrow = pyowm.timeutils.end_of_tomorrow()

        # Get the forecast data for the next day
        forecast_tomorrow = forecast.get_weathers_between(tomorrow, end_of_tomorrow)

        # Get the forecast for the next day
        forecast_tomorrow = forecast_tomorrow[0]

        # Include the forecast for the next day in the message
        message += f" The forecast for tomorrow is {forecast_tomorrow.get_temperature('celsius')['max']}°C and {forecast_tomorrow.get_detailed_status()}."

        dispatcher.utter_message(text=message)
        read_to_user(message)


