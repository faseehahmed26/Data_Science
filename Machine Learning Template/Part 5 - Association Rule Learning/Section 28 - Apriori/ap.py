#aproori

#importing the librRIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset=pd.read_csv("Market_Basket_Optimisation.csv")
transactions=[]
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
# Training apriori on the dataset
from apyori import apriori
rules = apriori(transactions,min_support=0.03,min_confidence=0.8,min_lift=3,min_length=2)

#Visualizing the results

results = list(rules)
