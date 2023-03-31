

# **Virtual Assistant**

This is a virtual assistant application that allows users to give instructions to their computer through speech recognition. The application has several features, including:

  

 - Pressing keyboard keys (e.g., Enter, Escape, Space, Arrow Down) 
  - Scrolling down on a webpage
   
  - Searching YouTube for a given query
   
   - Getting the current weather and tomorrow's forecast using the
   - OpenWeatherMap API
   
  - Fetching the latest news headlines from the NewsAPI

## Getting Started

To get started with the application, you need to install the required packages. You can do this by running the following command:



    pip install -r requirements.txt

Next, you need to set up your API keys for the OpenWeatherMap and NewsAPI services. You can do this by creating a .env file in the root directory of the project and adding the following lines:

    OWM_API_KEY=<YOUR_API_KEY>
    NEWSAPI_API_KEY=<YOUR_API_KEY>

Before running the application, you need to start the Rasa server for running custom actions. You can do this by running the following command in one terminal:

    `rasa run actions` 

Next, start the Rasa server with API enabled and CORS enabled by running the following command in another terminal:

    `rasa run --enable-api --cors "*"` 

Finally, start the voice recognition component of the application by running the following command in a third terminal:

    `python voice_recognition/main.py` 

Once the application is running, you can start giving instructions to your computer by speaking to the microphone. The application will transcribe your speech and use the Rasa framework to understand your intent. Based on your intent, the application will perform the appropriate action, such as pressing a keyboard key or searching YouTube.

Once the application is running, you can start giving instructions to your computer by speaking to the microphone. The application will transcribe your speech and use the Rasa framework to understand your intent. Based on your intent, the application will perform the appropriate action, such as pressing a keyboard key or searching YouTube.

  

## Features

**Pressing Keyboard Keys**

To press a keyboard key, you can say the name of the key (e.g., "Enter", "Escape", "Space", "Arrow Down"). The application will simulate the corresponding keyboard press.

  

**Scrolling Down on a Webpage**

To scroll down on a webpage, you can say "Scroll Down". The application will simulate scrolling down on the active webpage.

  

**Searching YouTube**

To search for a query on YouTube, you can say "Search for <QUERY> on YouTube". The application will open a new tab on your default browser and search for the given query on YouTube.

  

**Getting the Current Weather and Tomorrow's Forecast**

To get the current weather for your location, you can say "What's the weather like?". The application will use the OpenWeatherMap API to get the current weather and report back to you.

  

To get tomorrow's forecast for your location, you can say "What's the forecast for tomorrow?". The application will use the OpenWeatherMap API to get tomorrow's forecast and report back to you.

  

**Fetching the Latest News Headlines**

To fetch the latest news headlines for your location, you can say "What's in the news?". The application will use the NewsAPI to get the latest headlines and report back to you.

  

## Speech Recognition Component

The speech recognition component of the application is implemented using the SpeechRecognition package. The `recognize_speech_from_mic` function transcribes speech from the microphone and returns a dictionary with the following keys:

  

 - ***success*** - a boolean value indicating if the transcription was
   successful or not
   
  - ***error*** - a string containing an error message if the transcription
   failed, otherwise it is set to None
   
 -  ***transcription*** - a string containing the transcribed speech if the transcription was successful, otherwise it is set to `None`

The `read_to_user` function converts text to speech using the Google Text-to-Speech API and saves the speech as an MP3 file. The file is played and then deleted. The function accepts two parameters:

 - ***text*** -  a string containing the text to be converted to speech
 - ***language*** - a string indicating the language in which the text should   be spoken (default is English)

Contributors

Piotr Nowakowski - author