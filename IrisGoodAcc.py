# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SKOVuacX7FyALBzGrJ_BIbMqf_oRJ2DQ
"""

import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn import preprocessing
from tensorflow import keras

dataframe = pd.read_csv('https://raw.githubusercontent.com/sanjeshpathak/ml/master/iris.csv')

dataset = dataframe.values

X = dataset[:,0:4]


min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)

labels = dataset[:,4]

lists = []
for i in dataframe['flower']:
    if(i == 'Iris-setosa'):
        lists.append(0)
    if(i == 'Iris-versicolor'):
        lists.append(1)
    if(i == 'Iris-virginica'):
        lists.append(2)

Y = keras.utils.to_categorical(lists)
# Y = lists

X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)


model = tf.keras.Sequential([
  layers.Dense(128, activation='relu', input_shape=(4,)),
  layers.Dense(128, activation='relu'),
  layers.Dense(3, activation='sigmoid')
])

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

hist = model.fit(X_train, Y_train, batch_size=32, epochs=50, validation_data=(X_val, Y_val))