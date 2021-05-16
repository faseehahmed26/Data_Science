# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:35:36 2020

@author: Faseeh
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X=dataset.iloc[:, :-1].values
Y=dataset.iloc[:, 3].values
    

#Splitting the dataset into the training set and test set
 from sklearn.model_selection import train_test_split
 X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2,random_state=0)
 
 """"#Feature Scaling
 
 from sklearn.preprocessing import StandardScaler
 
 sc_X=StandardScaler()
 X_train=sc_X.fit_transform(X_train)
 X_test=sc_X.fit_transform(X_test)"""
 