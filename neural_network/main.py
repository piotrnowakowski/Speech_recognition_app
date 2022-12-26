import librosa
import numpy as np
import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model("model.h5")

def classify_audio(audio_path):
    # Load the audio file
    audio, sr = librosa.load(audio_path)
    # Compute the spectrogram
    spectrogram = librosa.feature.melspectrogram(audio, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
    # Convert the spectrogram to dB
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    # Normalize the spectrogram
    spectrogram_db = np.clip((spectrogram_db - db_min) / (db_max - db_min), 0, 1)
    # Reshape the spectrogram for the model input
    spectrogram_input = spectrogram_db[np.newaxis, ..., np.newaxis]
    # Classify the audio
    prediction = model.predict(spectrogram_input)
    # Check if the model predicts "ok google"
    if prediction[0][0] > 0.5:  # 0.5 is an arbitrary threshold
        # Run the function
        # HERE FUNCTION TO LISTEN
        pass

# Test the classify_audio function on an audio file
classify_audio("test.wav")
