import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import os

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img
                  
!wget -O data.zip https://github.com/JimGora/Classification/releases/download/Histopathology/Histopathology.zip
!unzip data.zip

path = './Histopatology/train/0'
rand_i = random.choice(os.listdir(path))
rand_img = f'{path}/{rand_i}'
load_img(rand_img)


import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.optimizers import Adam

data_dir = './Histopatology'
batch_size = 32
img_size = (512, 512)
num_classes = 4


train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    data_dir + '/train', target_size=img_size, batch_size=batch_size, class_mode='categorical')

validation_generator = validation_datagen.flow_from_directory(
    data_dir + '/validation', target_size=img_size, batch_size=batch_size, class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
    data_dir + '/test', target_size=img_size, batch_size=batch_size, class_mode='categorical')


base_model_V2 = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model_V2.trainable = False

model_V2 = tf.keras.Sequential([
    base_model_V2,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dense(num_classes, activation='softmax')])

lr = 0.001
model_V2.compile(optimizer=Adam(learning_rate=lr), loss='categorical_crossentropy', metrics=['accuracy'])

epochs = 20
model_V2.fit(train_generator, epochs=epochs, validation_data=validation_generator)


test_loss, test_accuracy = model_V2.evaluate(test_generator)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")