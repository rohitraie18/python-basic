import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
"""
# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape the data to include a channel dimension (grayscale images have 1 channel)
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Visualize the first image in the dataset
plt.imshow(train_images[0].reshape(28, 28), cmap='gray')
plt.title(f'Label: {train_labels[0]}')
plt.show()
"""

# Build the CNN model
model = models.Sequential()

# First convolutional layer
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Second convolutional layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Flatten the feature maps to feed into the dense layer
model.add(layers.Flatten())

# Fully connected layer
model.add(layers.Dense(64, activation='relu'))

# Output layer (for 10 digit classes)
model.add(layers.Dense(10, activation='softmax'))

# Print the model summary
model.summary()