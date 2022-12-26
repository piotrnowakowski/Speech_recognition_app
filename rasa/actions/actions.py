# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import keyboard
import pyautogui
import webbrowser
import time
from pyowm import OWM
import requests

#
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


class Escape(Action):
    def name(self):
        return "action_escape"
    def run(self, dispatcher, tracker, domain):
        keyboard.send("escape")
        dispatcher.utter_message(text="enter escape")

class Space(Action):
    def name(self):
        return "action_space"
    def run(self, dispatcher, tracker, domain):
        keyboard.send("space")
        print("space pressed")
        dispatcher.utter_message(text="space pressed")

class ArrowDown(Action):
    def name(self):
        return "action_arrow_down"
    def run(self, dispatcher, tracker, domain):
        keyboard.send("arrow_down")
        print("arrow down pressed")
        dispatcher.utter_message(text="arrow down pressed")
        
class ScrollDown(Action):
    def name(self):
        return "action_scroll_down"
    def run(self, dispatcher, tracker, domain):
        pyautogui.scroll(-100)

        # Send a message to the user
        dispatcher.utter_message(text="arrow down pressed and page scrolled down")

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


class OpenWeatherMapClient:
    def __init__(self, api_key):
        self.owm_client = OWM(api_key)

    def get_current_weather(self, location):
        # Send a request to the OpenWeatherMap API to get the current weather for the given location
        weather = self.owm_client.weather_at_place(location).get_weather()
        # Return the weather data
        return weather
    
    def get_user_location(self):
        # Set up the API URL and request headers
        api_url = "https://api.ipgeolocation.io/ipgeo"
        headers = {"API-Key": '2ae49291af8d453a917666db8d5ab3be'}

        # Send a request to the API to get the location of the user's device
        response = requests.get(api_url, headers=headers)

        # Parse the response data
        data = response.json()

        # Print the city and county
        return { 'city': data['city'], 'country': data['county']}


class GetWeatherAction(Action):
    def __init__(self):
        # Set up the OpenWeatherMap API client
        self.weather_client = OpenWeatherMapClient(api_key='2988f66310cb9fb07835c49b29d9b685')

    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):
        # Get the location from the user's message
        location = self.weather_client.get_user_location()
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


class GetWeatherAction(Action):
    def __init__(self):
        # Set up the OpenWeatherMap API client
        self.weather_client = pyowm.OWM('2988f66310cb9fb07835c49b29d9b685')

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


