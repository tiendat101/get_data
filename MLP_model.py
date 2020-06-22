import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
# from sklearn.cross_validation import train_test_split
from sklearn.metrics import roc_curve, auc
from keras.utils import to_categorical
import keras
from keras import initializers
import tensorflow as tf
import random 

np.random.seed(123)
tf.set_random_seed(123)

data = pd.read_csv('data_preprocessed.txt', header = None)
data = data.to_numpy()

np.random.shuffle(data)
indices = np.random.permutation(data.shape[0])
train_idx, test_idx = indices[:int(data.shape[0]*0.8)], indices[int(data.shape[0]*0.80):int(data.shape[0])]

train_data, test_data = data[train_idx,:], data[test_idx,:]
# print("train_data:", train_data)
# print("test_data", test_data)
X_train, Y_train = train_data[:,:7], train_data[:,7]
X_test, Y_test = test_data[:,:7], test_data[:,7]

Y_train_onehot = keras.utils.to_categorical(Y_train)

# print('First 3 labels: ', Y_train[3:20])
# print('\nFirst 3 labels (one-hot):\n', Y_train_onehot[3:20])

# initialize model
model = keras.models.Sequential()

# add input layer
model.add(keras.layers.Dense(
    units=50,
    input_dim=X_train.shape[1],
    kernel_initializer='glorot_uniform',
    bias_initializer=initializers.Constant(0.1),
    activation='tanh') 
)
# add hidden layer
model.add(
    keras.layers.Dense(
        units=50,
        input_dim=50,
        kernel_initializer='glorot_uniform',
        bias_initializer=initializers.Constant(0.1),
        activation='tanh')
    )

# add output layer

model.add(
    keras.layers.Dense(
        units=Y_train_onehot.shape[1],
        input_dim=50,
        kernel_initializer='glorot_uniform',
        bias_initializer=initializers.Constant(0.1),
        activation='softmax')
    )
# define SGD optimizer
sgd_optimizer = keras.optimizers.SGD(
    lr=0.001, decay=1e-3, momentum=0.9
)

# compile model
model.compile(
    optimizer=sgd_optimizer,
    loss='categorical_crossentropy'
)


# train model
history = model.fit(
    X_train, Y_train_onehot,
    batch_size=64, epochs=100,
    verbose=1, validation_split=0.1
)
# print('First 3 labels: ', Y_train[:10])
# print('\nFirst 3 labels (one-hot):\n', Y_train_onehot[:10])
# y_train_pred = model.predict_classes(X_train, verbose=0)
# print('First 3 predictions: ', y_train_pred[:10])
# calculate training accuracy
y_train_pred = model.predict_classes(X_train, verbose=0)
correct_preds = np.sum(Y_train == y_train_pred, axis=0)
train_acc = correct_preds / Y_train.shape[0]

print(f'Training accuracy: {(train_acc * 100):.2f}%')

# calculate testing accuracy
y_test_pred = model.predict_classes(X_test, verbose=0)
correct_preds = np.sum(Y_test == y_test_pred, axis=0)
test_acc = correct_preds / Y_test.shape[0]

print(f'Test accuracy: {(test_acc * 100):.2f}%')
y_test_pred = model.predict_classes(X_test[:], verbose=0)
print(y_test_pred[:])
print(Y_test[:])

