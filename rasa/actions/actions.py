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
        if 'youtube' in user_input:
            user_input = user_input.split('youtube')[1]

        # Open YouTube in a new tab
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query={}".format(user_input))

        # Send a message to the user
        dispatcher.utter_message(text="Searching for '{}' on YouTube".format(user_input))



