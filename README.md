# Customer-Segmentation-using-Clustering-Algorithms
1. Customer segmentation is the process of dividing customers into groups based on common characteristics such as recency, expected transaction amount, number of transactions etc. so companies can market to each group effectively and appropriately.
2. In clustering we group customers into meaningful clusters. In a sense, labels are associated with clusters , but these category labels are data driven; that is, they are obtained solely from the data.
3. Our problem statement deals with fetching the retail data from the enterprise.This data has to be stored in the oracle database in the form of dataframes,which then can be fetched for processing.
4. In our case we use three clustering algorithms: "K-MEANS","HIERARCHICAL CLUSTERING" and "SPECTRAL CLUSTERING" algorithms.
5. We then store the clustered results(labelled data) back into the database.This final result can then be used to let the retail enterprise to know which group of customers to target in order to earn better profits.
6. The outcome of the project is that through the clustered data we can analyze the characteristics of different group of customers.



## 1. Execution time for different number of records with clusters K=5
![image](https://user-images.githubusercontent.com/15854238/147630518-b339a2ce-ed17-497e-aebc-bcc2667b6653.png)

From the above graph, The time taken by K-means algorithm is very less when compared to spectral and hierarchical algorithm. The time taken by hierarchical for the same number of records is double the time taken by K-means. Hence K-means is the most efficient algorithm for clustering the data. 

## 2. Execution time for different number of clusters
![image](https://user-images.githubusercontent.com/15854238/147630595-10dad709-a66d-4392-a870-fcb481968679.png)
From the above graph we can derive the information that K-means takes the least amount of time for any number of clusters when compared to spectral clustering and hierarchical clustering.

## 3. Comparison between withiness and betweeness with different number of clusters
![image](https://user-images.githubusercontent.com/15854238/147630622-1af3c9f1-bf22-4d50-9111-bf181a7c4dc9.png)

## 4. Optimal K value using Elbow method
![image](https://user-images.githubusercontent.com/15854238/147630650-539338da-9311-4a17-91c8-1f3ed76d3af1.png)

The value K=4 and K=5 are equally good values for K. But K=5 has a lower ratio of withiness to betweeness than the ratio for K=4, hence K=5 is the most optimal value for the given data.




