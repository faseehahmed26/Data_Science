# MUltiple Linear Regression



#Importing the dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X=dataset.iloc[:, :-1].values
Y=dataset.iloc[:, 4].values
    

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()


# Avoiding The Dummy Variable Trap
X=X[:,1:]
#Splitting the dataset into the training set and test set
 from sklearn.model_selection import train_test_split
 X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2,random_state=0)
 
 """"#Feature Scaling
 
 from sklearn.preprocessing import StandardScaler
 
 sc_X=StandardScaler()
 X_train=sc_X.fit_transform(X_train)
 X_test=sc_X.fit_transform(X_test)"""
 
#Fitting Multiple Linear Regrseeion to the training set
 from sklearn.linear_model import LinearRegression
 regressor=LinearRegression()
 regressor.fit(X_train,Y_train)
 
 # Predicting the test set results
 
Y_pred=regressor.predict(X_test)

# Building the optimal model using backward elimination

import statsmodels.api as sm

X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)
X_opt=X[:,[0,1,2,3,4,5]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,1,3,4,5]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,3,4,5]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,3,5]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,3]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
