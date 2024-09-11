from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import keyboard
import pyautogui
import webbrowser
import time
import pyowm
from pyowm import OWM
import requests
import time
from .mic_functions.text_to_sound import read_to_user
from .additional_functions.get_user_location import get_user_location
from .additional_functions.weather_client import OpenWeatherMapClient
from dotenv import load_dotenv
import os

load_dotenv()

OWM_API_KEY = os.getenv('OWM_API_KEY')
NEWSAPI_API_KEY = os.getenv('NEWSAPI_API_KEY')

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
class GetWeatherAction(Action):
    def __init__(self):
        # Set up the OpenWeatherMap API client
        self.weather_client = OpenWeatherMapClient(api_key=OWM_API_KEY)
    def name(self):
        return "action_get_current_weather"
    def run(self, dispatcher, tracker, domain):
        # Get the location from the user's message
        location = get_user_location()
        dispatcher.utter_message(location)
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
        self.weather_client = OpenWeatherMapClient(api_key=OWM_API_KEY)
        pass
    
    def name(self):
        return "action_get_tommorow_weather"

    def run(self, dispatcher, tracker, domain):
        # Get the location from the user's message
        location = get_user_location()
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
        message += f" The forecast for tomorrow is {forecast_tomorrow.get_temperature('celsius')['max']}celsius degrees and {forecast_tomorrow.get_detailed_status()}."

        dispatcher.utter_message(text=message)
        read_to_user(message)

##################################################################################
class ActionFetchNews(Action):
    def name(self):
        return "action_fetch_news"
    
    def run(self, dispatcher, tracker, domain):
        
        # Get the user's location and topic preferences from the tracker
        location = get_user_location
        topic = tracker.get_slot("topic")
        
        # Define the NewsAPI endpoint and parameters

        url = f"https://newsapi.org/v2/top-headlines?country={location['country']}&apiKey={NEWSAPI_API_KEY}"
        
        # Send a GET request to the NewsAPI endpoint
        response = requests.get(url)
        
        # Handle the response based on the HTTP status code
        if response.status_code == 200:
            # Parse the response JSON to extract the news headlines
            data = response.json()
            headlines = [article["title"] for article in data["articles"]]
            
            # Format the headlines as a string and send them to the user
            message = "Here are the latest news headlines:\n\n" + "\n".join(headlines)
            dispatcher.utter_message(text=message)
        else:
            # If there was an error, send an error message to the user
            dispatcher.utter_message(text="Sorry, I could not fetch the news at this time. Please try again later.")
        
        return []


class ActionFetchNews(Action):
    def name(self):
        return "action_fetch_specifictopic_news"
    
    def run(self, dispatcher, tracker, domain):
        
        # Get the user's topic preference from the tracker
        topic = tracker.get_slot("topic")
        
        # Define the NewsAPI endpoint and parameters
        try:
            with open('newsapi_key.txt', "r") as f:
                api_key = f.read().strip()
        except:
            read_to_user("There was an error with reading API key")
        url = f"https://newsapi.org/v2/top-headlines?category={topic}&apiKey={NEWSAPI_API_KEY}"
        
        # Send a GET request to the NewsAPI endpoint
        response = requests.get(url)
        
        # Handle the response based on the HTTP status code
        if response.status_code == 200:
            # Parse the response JSON to extract the news headlines
            data = response.json()
            headlines = [article["title"] for article in data["articles"]]
            
            # Format the headlines as a string and send them to the user
            message = "Here are the latest news headlines:\n\n" + "\n".join(headlines)
            dispatcher.utter_message(text=message)
        else:
            # If there was an error, send an error message to the user
            dispatcher.utter_message(text="Sorry, I could not fetch the news at this time. Please try again later.")
        
        return []

import time

class ActionPomodoro(Action):
    def name(self):
        return "action_pomodoro"
    
    def run(self, dispatcher, tracker, domain):
        # Get the current cycle from the tracker
        current_cycle = tracker.get_slot("current_cycle") or 1
        
        # Set the timer based on the current cycle

        # Pomodoro cycle: 25 minutes
        duration = 25 * 60
        message = "Pomodoro started!"
        read_to_user(message)
        # Start the timer
        start_time = time.time()
        end_time = start_time + duration
        while time.time() < end_time:
            time.sleep(60)
        read_to_user("Pomodor ended break starting")
        if current_cycle % 4 == 1:
            breaktime = 15*60
            tracker.slots["current_cycle"] = 1
        else:
            breaktime = 5*60
        start_time = time.time()
        end_time = start_time + breaktime
        # Update the tracker with the new cycle and end time
        tracker.slots["current_cycle"] = current_cycle + 1
        
        # Send a message to the user and read it aloud
        dispatcher.utter_message(text=message)
        read_to_user("break ended. If You want to start pomodoro tell me")
        
        return []


