import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

#mnist = tf.keras.datasets.mnist

# x_train hand written data, y_train is the classification
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# # only want to normalize the pixels
# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)

# model = tf.keras.models.Sequential()

# # Layers
# model.add(tf.keras.layers.Flatten(input_shape=(28,28))) # 28x28 pixels
# model.add(tf.keras.layers.Dense(128, activation="relu")) # Dense layer, rectify linear unit
# model.add(tf.keras.layers.Dense(10, activation='softmax')) # All 10 neurons add up to one 

# # Compile
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# # Train model
# model.fit(x_train, y_train, epochs=3)

# model.save('handDigitRecon.keras')

model = tf.keras.models.load_model('handDigitRecon.keras')

imageNumber = 1

while os.path.isfile(f"digits/digit{imageNumber}.png"):
    try:
        image = cv2.imread(f"digits/digit{imageNumber}.png")[:,:,0]
        image = np.invert(np.array([image]))
        prediction = model.predict(image)
        print(f"The number is probbably {np.argmax(prediction)}") # which nueron has the higest prediction
        plt.imshow(image[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("Error")
    finally:
        imageNumber += 1