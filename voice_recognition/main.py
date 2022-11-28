import random
import time
from rasa_connection import send_text_to_rasa
import speech_recognition as sr
from mic_functions.mic import recognize_speech_from_mic
from mic_functions.text_to_sound import read_to_user
import os
os.add_dll_directory(os.getcwd())

if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit


    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print(microphone)

    # get a random word from the list

    # format the instructions string
    instructions = ("You can give me an instruction on what to do on your computer")

    # show instructions and wait 3 seconds before starting the game
    print(instructions)
    read_to_user(instructions)
    time.sleep(3)

    for i in range(4):
        print('Guess {}. Speak!'.format(i+1))
        guess = recognize_speech_from_mic(recognizer, microphone)
        if guess["transcription"]:
            #TODO rasa connection
            send_text_to_rasa(guess["transcription"])
        if not guess["success"]:
            read_to_user("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
        if guess["error"]:
            read_to_user("ERROR {}".format(guess["error"]))
            break

        # check the transcription
        read_to_user("You said: {}".format(guess["transcription"]))
        print("You said: {}".format(guess["transcription"]))

   