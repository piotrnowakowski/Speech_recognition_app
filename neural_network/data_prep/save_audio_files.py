import speech_recognition as sr
import random
import hashlib

# Set up the recognizer
recognizer = sr.Recognizer()

# Collect audio from the microphone
with sr.Microphone() as source:
    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)
    # Listen for audio
    audio = recognizer.listen(source)

# Convert the audio to text
try:
    text = recognizer.recognize_google(audio)
    print(text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error making request: {0}".format(e))

# Check if the text is "ok google"
if text == "ok google":
    # Generate a hash of the audio data
    hash_val = hashlib.sha256(audio.get_wav_data()).hexdigest()
    # Save the audio file and label it with the random number and hash
    with open(f"ok_google_{hash_val}.wav", "wb") as f:
        f.write(audio.get_wav_data())
