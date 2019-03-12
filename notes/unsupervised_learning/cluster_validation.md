# **Cluster Validation**

There are three categories for cluster validation indices:
* External indices: scoring methods that we use if the data was originally labeled.
* Internal indices: when we don't have any labels.
* Relative indices: which of 2 clustering structures is better in some sense.

Cluster validation usually looks at **compactness** (how similar the elements of a cluster are)  and **separability** (how far or distinct clusters are from each other).

## **External validation indices**

Some indices include:
|Index| Range|
|---|---|
| Adjusted Rand Score |  [-1,1] |
| Fawlks and Mallows  |  [0,1] |
| NMI measure         |  [0,1] |
| Jaccard             |  [0,1] |
| F-measure           |  [0,1] |
| Purity              |  [0,1] |

### **Adjusted Rand Score**

![Rand Index](/images/Rand_index_formula.png)

* **a** is the number of pairs in the same cluster C (original labels) and the same cluster K (our new cluster labels).

* **b** is number of pairs in a different cluster C and remain in a different cluster in K. It looks at the pairs that were in different clusters in C and are still in different clusters in K.

* **n** is the number of samples/ points

The **Adjusted Rand Index** is the same, except we just discount the expected index.

![Rand Index](/images/adjusted_rand_index_formula.png)

**A value close to 1 is good.**

## **Internal validation indices**

Some indices include:
|Index| Range|
|---|---|
| Silhouette index |  [-1,1] |
| Calinski-Harabasz  |   |
| BIC         |   |
| Dunn             |   |


### **Silhouette Coefficient**

The silhouette coefficient measures how tightly grouped the samples in the clusters are. Also it looks at the distance between clusters and penalizes when there is not enough distance in between. We can apply the following three steps:

1. Calculate the cluster cohesion **a**, as the average distance between a sample x and all the other points in the same cluster.

2. Calculate the cluster separation **b** from the next closest cluster as the average distance between the sample x and all the samples in the nearest cluster.

3. Calculate the shilhouette as the difference between cluster cohesion and separation divided by the greater of the two.

![Silhouette coefficient](/images/silhouette_coefficient.png)

Each point in the dataset has a silhouette coefficient, therefore the coefficient is calculated by the averaging the results for each point in the distribution. 

**Warning**: 
* Silhouette coefficient should not be used with DBSCAN, as it doesn't understand the concept of noise, and it will get penalized a lot even if it does well. For DBSCAn the [Density-based Clustering Validation](https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=83C3BD5E078B1444CB26E243975507E1?doi=10.1.1.707.9034&rep=rep1&type=pdf) should be used.
* Silhouette coefficient won't do very good on some distributions, even if the data is properly separated (2 rings example). THat is because it looks at how tight the samples of a cluster are, and if the cluster has a funny shape not exactly all tight up, it will give unpredictable results, even if the data is perfectly separated.





## **Resources**

[Python Machine Learning Second Edition](https://www.amazon.com/Python-Machine-Learning-scikit-learn-TensorFlow/dp/1787125939)

[Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)