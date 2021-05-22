#ANN

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import tensorflow as tf
#tf.__version__

# Part 1 - Data Preprocessing

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

# Encoding categorical data

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
LabelEncoder_X_1=LabelEncoder()
X[:,1]=LabelEncoder_X_1.fit_transform(X[:,1])
LabelEncoder_X_2=LabelEncoder()
X[:,2]=LabelEncoder_X_2.fit_transform(X[:,2])
onehotencoder=OneHotEncoder(categorical_features=[1])
X=onehotencoder.fit_transform(X).toarray()
X=X[:,1:]
# Label Encoding the "Gender" column
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])
print(X)
# One Hot Encoding the "Geography" column
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
print(X)


# Part 2 - Building the ANN

#Importing the keras library
import keras
from keras.models import Sequential
from keras.layers import Dense

#Initializing the ANN
classifier=Sequential()

#Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim=6,init='uniform',activation='relu',input_dim=11))

#Adding the second hidden layer
classifier.add(Dense(output_dim=6,init='uniform',activation='relu'))
#Adding the output layer
classifier.add(Dense(output_dim=1,init='uniform',activation='sigmoid'))

#COmpiling the ANN
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
#Fitting the ANN to training set
classifier.fit(X_train,y_train,batch_size=10,nb_epoch=100)

#Fitting the test set results
y_pred=classifier.predict(X_test)
y_pred=(y_pred > 0.5)

#Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
