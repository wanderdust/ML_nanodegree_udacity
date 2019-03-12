# **k-Means**

K-means clustering is an unsupervised learning technique to group data into clusters. K-means is very efficient compared to other clustering methods, which makes it very popular. It belongs to the category of **prototype-based clustering**.

While k-means is very good at identifying clusters with spherical shape, one of the drawbacks is that we have to specify the number of clusters a priori.


The way it works is the following:
1. First we decide how many clusters we want, so that we can randomly plot as many centroids as clusters we want.

![Random centroids](/images/k_means_ex_1.png)

2. Then it calculates the squared distances from the center to all the points, and moves towards the direction that minimizes it.

![updated centroids](/images/k_means_ex_2.png)

3. Once updated we assign the closest points to the centroid as part of the cluster. Then we repeat the process until we get to a good classification.

![Good classification](/images/k_means_ex_3.png)

## **Challenges of K-means**

* **Randomness**: because of the the centroids are palced at random at the beggining it can result in different results if we run the same example multiple times. In some cases the algorithm will find a local minimum that's not very good due to this random initialization. That's why it is a good a idea to run the example a few times until we reach a satisfying clustering.

* **Works well with circular data**: it works really well with circular data because of the nature of the squared distance. However it might not perform well with other cluster distributions.




 ## **Resources**
 Udacity: [Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)

 Naftali Harris [www.naftaliharris.com](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/)