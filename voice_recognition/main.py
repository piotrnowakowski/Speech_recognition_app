import random
import time
from rasa_connection import send_text_to_rasa
import speech_recognition as sr
from mic_functions.mic import recognize_speech_from_mic
from mic_functions.text_to_sound import read_to_user
import os
os.add_dll_directory(os.getcwd())

if __name__ == "__main__":
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print(microphone)

    instructions = ("You can give me an instruction on what to do on your computer")

    # pokazujemy instrukcje i czekamy 2 sekundy przed rozpoczęciem nasłuchiwania
    read_to_user(instructions)
    time.sleep(2)

    for i in range(4):
        guess = recognize_speech_from_mic(recognizer, microphone)
        if guess["transcription"]:
            # przesłanie tekstu do systemu Rasa w celu przetworzenia
            send_text_to_rasa(guess["transcription"])
        if not guess["success"]:
            read_to_user("I didn't understand that. Repeat please\n")

        # if there was an error, stop the game
        if guess["error"]:
            read_to_user("there was an ERROR {}".format(guess["error"]))
            break

        # check the transcription
        read_to_user("You said: {}".format(guess["transcription"]))
        print("You said: {}".format(guess["transcription"]))

   