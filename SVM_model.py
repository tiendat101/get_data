import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

np.random.seed(123)

data = pd.read_csv('data_preprocessed.txt', header = None)
# print(data.shape)
data = data.to_numpy()

np.random.shuffle(data)
indices = np.random.permutation(data.shape[0])
train_idx, test_idx = indices[:int(data.shape[0]*0.8)], indices[int(data.shape[0]*0.80):int(data.shape[0])]

train_data, test_data = data[train_idx,:], data[test_idx,:]
# print("train_data:", train_data)
# print("test_data", test_data)
X_train, Y_train = train_data[:,:7], train_data[:,7]
X_test, Y_test = test_data[:,:7], test_data[:,7]

# train model 
svclassifier = SVC(kernel='rbf')
svclassifier.fit(X_train, Y_train)

y_pred = svclassifier.predict(X_test)
print(y_pred)
print(confusion_matrix(Y_test,y_pred))
print(classification_report(Y_test,y_pred))