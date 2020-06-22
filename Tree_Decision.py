import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
np.random.seed(123)

data = pd.read_csv('data_preprocessed.txt', header = None)
# print(data.shape)
data = data.to_numpy()

np.random.shuffle(data)
indices = np.random.permutation(data.shape[0])
train_idx, test_idx = indices[:int(data.shape[0]*0.70)], indices[int(data.shape[0]*0.70):int(data.shape[0])]

train_data, test_data = data[train_idx,:], data[test_idx,:]
# print("train_data:", train_data)
# print("test_data", test_data)
X_train, Y_train = train_data[:,:7], train_data[:,7]
X_test, Y_test = test_data[:,:7], test_data[:,7]

# # train model

# # Create Decision Tree classifer object
# clf = DecisionTreeClassifier()

# # Train Decision Tree Classifer
# clf = clf.fit(X_train, Y_train)

# #Predict the response for test dataset
# y_pred = clf.predict(X_test)

# print("Accuracy:", metrics.accuracy_score(Y_test, y_pred))

#------------optimize--------------
# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=2)

# Train Decision Tree Classifer
clf = clf.fit(X_train, Y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy: %.2f" % (metrics.accuracy_score(Y_test, y_pred)))