#Apriori

#Data Preprocessing

#install.packages('arules')

library(arules)
dataset=read.csv('Market_Basket_Optimisation.csv',header = FALSE)
dataset=read.transactions('Market_Basket_Optimisation.csv',sep=',',rm.duplicates = TRUE)
summary(dataset)

#Training Aprirori on the dataset
rules=apriori(data = dataset,parameter = list(support=0.003 ,confidence=0.2))

#Visualizing the results

inspect(sort(rules, by = 'lift')[1:10])

