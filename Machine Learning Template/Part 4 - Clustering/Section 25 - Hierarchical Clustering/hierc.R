#HC

#Importing the mall dataset
dataset <- read.csv("Mall_Customers.csv")
X <- dataset[4:5]

#Using the dendogram to find the optimal number of clusters


dendrogram=hclust(dist(X,method = 'euclidean'),method = 'ward.D')
plot(dendrogram,
           main=paste('Dendogram'),
         xlab='Customers',
          ylab='"euclidean Distances')
#FItting hierachial clustering to th emall dataset

hc=hclust(dist(X,method = 'euclidean'),method = 'ward.D')
y_hc=cutree(hc,5)


#Visualizing the cluster

clusplot(X,
         y_hc,
         lines = 0,
         shade=TRUE,
         color=TRUE,
         labels = 2,
         plotchar = FALSE,
         span=TRUE,
         main=paste("CLuster of clients"),
         xlab="Annual Income",
         ylab="Spending SCore"
)
