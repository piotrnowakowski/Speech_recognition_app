from gtts import gTTS
import os
import time
# This module is imported so that we can 
# play the converted audio
os.add_dll_directory(os.getcwd())
import vlc
import playsound

def read_to_user(text):
    language = 'en'
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("temp.mp3")
    
    # Playing the converted file
    #os.system("mpg321 temp.mp3")
    #p = vlc.MediaPlayer(r'C:\Users\pites2\Desktop\Inzynierka\voice_recognition\temp.mp3')
    playsound.playsound(r'C:\Users\pites2\Desktop\Inzynierka\voice_recognition\temp.mp3', True)
    os.remove("temp.mp3")


    