import os
import librosa
import numpy as np
import matplotlib.pyplot as plt

# Set the path to the folder containing the audio files
audio_folder = "path/to/audio/folder"

# Set the file extension of the audio files (e.g., "wav", "mp3")
file_ext = "wav"

# Set the parameters for the spectrogram
n_fft = 2048  # window size for the FFT
hop_length = 512  # number of samples to advance the window each time
n_mels = 128  # number of Mel bands to generate

# Set the parameters for the spectrogram plot
db_min = -100  # minimum decibel value for the plot
db_max = 10  # maximum decibel value for the plot

# Loop through all the audio files in the folder
for file in os.listdir(audio_folder):
    # Check if the file is an audio file with the correct file extension
    if file.endswith(file_ext):
        # Load the audio file
        audio, sr = librosa.load(os.path.join(audio_folder, file))
        # Compute the spectrogram
        spectrogram = librosa.feature.melspectrogram(audio, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
        # Convert the spectrogram to dB
        spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
        # Normalize the spectrogram
        spectrogram_db = np.clip((spectrogram_db - db_min) / (db_max - db_min), 0, 1)
        # Save the spectrogram as an image file
        plt.imsave(f"{file}.png", spectrogram_db, cmap="magma")
