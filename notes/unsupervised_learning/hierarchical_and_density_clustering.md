 # **Hierarchical and Density Based Clustering**

 # **Hierarchical Clustering**

 Hierarchical clustering or Agglomerative Clustering consists on finding the nearest clusters and merging them together. We keep doing this until we end up with a single cluster that we can then decide to break into as many clusters as we want.

 ### **Single link clustering**

 Single link cluster makes clusters by grouping the closest points from each cluster. The process is as follows:

 First we consider every point in the plot as a cluster. For each cluster we compute the distances from this cluster and all other clusters.

![Single link clustering](/images/single_link_clustering_ex_1.png)

 Then we choose the smallest distance between the two clusters, and join them together as 1 cluster. The distance between two clusters with multiple points each, is the distance between the two closest points in the clusters.

 ![Single link clustering](/images/single_link_clustering_ex_2.png)

 We then repeat the process by searching for the clusters that are closest to each other. Repeat this until we get a single top class cluster.

  ![Single link clustering](/images/single_link_clustering_ex_3.png)

  These reperesentations of the hierarchical clustering are called dendograms, and are a good visualization of how the data has been clustered. 

  Once the algorithm has finished the clustering we can decide how many clusters we want, and simply move down from the top of the dendogram until we have as many clusters as we want.

  **We need to specify the number of clusters we want beforehand**

  Comparison with K-means

  ![Single link clustering](/images/single_link_vs_kmeans.png)



  ### **Complete link clustering**

Same as single link clustering, except that the distance between 2 clusters is the distance from the furthest points of the cluster. This type of approach generates compact clusters.

A problem with this approach is that it only takes into consideration the furthest points, which is not always the most helpful thing.

### **Average link clustering**

The distance is calculated by the average of all the points from a cluster to the average of all the points to the other clusters.

### **Ward's Method**

This method attempts to minimize variance when merging 2 clusters.

First it calculates a central point between two clusters by calculating the average of all the points in the two clusters.

![Wards Method](/images/wards_method_ex_1.png)

Then it calculates the distance between each point and the center point, each raised to the power of two.

![Wards Method](/images/wards_method_ex_2.png)

Finally we want to subtract the variance already existing in the clusters. We do that by estimating the central point of each cluster (the average of all points in the cluster) and subtracting the distance of each point in the cluster to the central point. 

![Wards Method](/images/wards_method_ex_3.png)

We do this for all the clusters, and the ones that have the smallest error function (distances) will get merged together.


## **Pros And Cons of Hierachical Clustering**

**Advantages**

* Very informative and easy to visualize
* Potent when dataset contains real hierarchical data (eg. Biological Evolution)

**Disadvantages**

* Sensitive to noise and outliers
* Computationally expensive

***

# **Density Based Scan Clustering**

Density based scan creates clusters in areas where there is a minimun number of points within a radius. If these conditions are not met, the point will be considered as noise. This method works really well with noisy data.

### **DBSCAN**

We choose a point and look around it given a max radius. If this point has a minimum of *n* points within the radius (epsilon) it will be considered as a the core point of the clusters. The points around it will be considered border points. If it doesn't meet the requirements, they get considered noise.

![DBScan](/images/dbscan_ex_1.png)

We do this for all the points. All the core points that merge with each other will merge into a bigger cluster

![DBScan](/images/dbscan_ex_2.png)

Comparison of DBSCAN vs K-means

![DBScan vs k means](/images/dbscan_vs_kmeans.png)

## **Pros and Cons of DBSCAN**

**Advantages**
* No need to specify the number of clusters
* Flexibility in shape and sizes
* Able to deal with noise

**Disadvantages**
* Border points that are reachable from two clusters are given to the one that sees it first.
* FInds it difficuult for clusters with varying densities.





 ## **Resources**
 Udacity: [Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)

 Naftali Harris [www.naftaliharris.com](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/)


