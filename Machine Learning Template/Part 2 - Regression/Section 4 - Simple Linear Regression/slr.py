# SImple Linear Regression


#importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:, :-1].values
Y=dataset.iloc[:, 1].values
    

#Splitting the dataset into the training set and test set
 from sklearn.model_selection import train_test_split
 X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=1/3,random_state=0)
 
 """"#Feature Scaling
 
 from sklearn.preprocessing import StandardScaler
 
 sc_X=StandardScaler()
 X_train=sc_X.fit_transform(X_train)
 X_test=sc_X.fit_transform(X_test)"""
 
 #Fitting the Simple Linear Regression to the training Set
 from sklearn.linear_model import LinearRegression
 regressor=LinearRegression()
 regressor.fit(X_train,Y_train)
 
 # Predicting the test set results
 Y_pred=regressor.predict(X_test)
 
 # Visualizing the training set results
 
 plt.scatter(X_train,Y_train,color='red')
 plt.plot(X_train,regressor.predict(X_train),color='blue')
 plt.title('Salary vs Experience(Training set')
 plt.xlabel('Years of Experience')
 plt.ylabel('Salary')
 plt.show()
 
 
  # Visualizing the test set results
 
 plt.scatter(X_test,Y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
 plt.title('Salary vs Experience(Test set')
 plt.xlabel('Years of Experience')
 plt.ylabel('Salary')
 plt.show()