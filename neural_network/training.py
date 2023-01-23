import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set the path to the folder containing the spectrogram images
image_folder = "path/to/spectrogram/images"

# Set the image size (height and width in pixels)
img_size = (128, 128)

# Set the batch size for training
batch_size = 32

# Set the number of classes
num_classes = 2  # "ok google" and "not ok google"

# Set the number of epochs
num_epochs = 10

# Set the learning rate
learning_rate = 0.001

# Load the pre-trained model
base_model = tf.keras.applications.MobileNetV2(input_shape=img_size+(3,), include_top=False, weights='imagenet')

# Freeze the base model layers
base_model.trainable = False

# Create a new model on top of the base model
model = Sequential([
    base_model,
    Flatten(),
    Dense(1024, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
              loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])

# Create the data generators
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

validation_datagen = ImageDataGenerator(rescale=1./255)

# Create the data flow from the directories
train_generator = train_datagen.flow_from_directory(os.path.join(image_folder, "train"),
                                                    target_size=img_size,
                                                    batch_size=batch_size,
                                                    class_mode='sparse')

validation_generator = validation_datagen.flow_from_directory(os.path.join(image_folder, "validation"),
                                                              target_size=img_size,
                                                              batch_size=batch_size,
                                                              class_mode='sparse')

# Train the model
model.fit(train_generator,
          epochs=num_epochs,
          validation_data=validation_generator)

# Save the model
model.save("trained.h5")

# Load the saved model
#loaded_model = tf.keras.models.load_model("model.h5")
