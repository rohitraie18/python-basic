"""
#Task 1
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Flatten the 28x28 input images
    layers.Dense(128, activation='relu'),  # First hidden layer with 128 neurons and ReLU activation
    layers.Dense(10, activation='softmax') # Output layer with 10 neurons (for 10 digit classes)
])

# Print the model summary
model.summary()



#Task 2
# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
"""

#Task 3
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize the images to a range of 0 to 1 by dividing by 255
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# Flatten the images from 28x28 to 784 (for the input layer)
train_images = train_images.reshape((train_images.shape[0], 784))
test_images = test_images.reshape((test_images.shape[0], 784))

# Train the model
history = model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))



#task 5
import matplotlib.pyplot as plt

# Example training history data
history = {
    'loss': [0.6, 0.5, 0.4, 0.3, 0.2],  # Sample training loss values
    'val_loss': [0.65, 0.55, 0.45, 0.35, 0.25],  # Sample validation loss values
    'accuracy': [0.7, 0.75, 0.8, 0.85, 0.9],  # Sample training accuracy
    'val_accuracy': [0.68, 0.72, 0.78, 0.83, 0.88]  # Sample validation accuracy
}

# Plotting the loss
plt.figure(figsize=(10, 6))
plt.plot(history['loss'], label='Training Loss')
plt.plot(history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()