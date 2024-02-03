from gtts import gTTS
import os
import time
#os.add_dll_directory(os.getcwd())
import playsound

def read_to_user(text, language = 'en'):
    """
    Funkcja przyjmuje dwa parametry:
    text: ciąg znaków zawierający tekst, który ma być odczytany użytkownikowi.
    language: oznacza język, w którym tekst będzie odczytany, domyślnie jest to angielski
    Konwertuje podany tekst na mowę za pomocą biblioteki Google Text-to-Speech, zapisuje mowę jako plik MP3, odtwarza plik MP3
    i następnie go usuwa.
    """
    
    # Przekazywanie tekstu i języka do silnika
    # slow=False konwertowany audio będzie miał wysoką prędkość
    myobj = gTTS(text=text, lang=language, slow=False)

    # Zapisywanie konwertowanego audio w pliku mp3 o nazwie
    myobj.save("temp.mp3")

    # Odtwarzanie konwertowanego pliku
    playsound.playsound(r'C:\Users\pites2\Desktop\Inzynierka\voice_recognition\temp.mp3', True)
    os.remove("temp.mp3")

    