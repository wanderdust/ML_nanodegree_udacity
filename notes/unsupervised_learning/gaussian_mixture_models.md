# **Gaussian Mixture Models**

Gaussian Mixture Models assume that each cluster follows a certain statistical distribution. A lot of data follows a normal distribution, which is the gaussian distribution.

## **Recap: Gaussian Distribution**

The gaussian distribution follows the bell curve, where most data is found around a most common value.

![Gaussian Distribution](/images/gaussian_distribution.png)

The gaussian distribution is defined by the mean and the standard deviation. A gussian distribution has **68%** of the distribution between the range of _(mean - 1*std)_ and _(mean + 1*std)_

![Gaussian Distribution](/images/gaussian_distribution_2.png)

Between _(mean - 2*std)_ and _(mean + 2*std)_ **95%** of the distribution can be found. And between _(mean - 3*std)_ and _(mean + 3*std)_, **99%** of the data can be found.

## **Gaussian Mixture**

GM finds a mixture of gaussian distributions in a dataset. This means that it finds a pattern of several gaussian bells, and separate them into individual bells. Each bell is considered a cluster. A point will belong to the bell that it looks more likely to belong to. 

GM is soft clustering algorithm, which means that each point in the dataset will belong to all the cluster in different proportions. There is not one unique cluster for each point.

### **Expectation Maximization Algorithm**

#### **1. Initialize the Distributions**

We need to initialize the distribution by giving them a mean, and a standard deviation. There are two ways that this can be done:
* Naive way: set them to the average and mean of the dataset itself.
* Run k-means to get the clusters and use that data to initialize the gaussian distribution.

#### **2. Soft Cluster the Data Points - Expectation**

We need to assign the _membership_ numbers for the points to the initial clusters. We can use a formula for this, which measures how much a point belongs to a specific cluster.

![Gaussian Distribution](/images/membership_gaussian_formula.png)

The function probabilities are given by the probability density function of a gaussian distribution:

![Gaussian Distribution](/images/prob_density_function.png)

We calculate this for all three parts of the equation, and we get a result, which will be the membership of a point to a cluster.

#### **3. Re-estimate Parameters of Gaussians; Maximization**

The goal on this step is to take everything that was produced in step two, and use it as an input for this step. For this step we need to calculate the new mean and variance for the cluster.
* The mean gets calculated by the weigred average of all the points in the clusters. This means multiplying each point by their membership to the cluster and dividing it by the sums of the memberships.

![Gaussian Distribution](/images/gm_new_mean.png)

* The variance gets calculated by doing a weighted version of how the variance get originally calulated (square distance from the mean). The new variance is then the variance multiplied by the membership, and divided by the sum of the memberships.

![Gaussian Distribution](/images/gm_new_variance.png)

#### **4. Evaluate Log-Likelihood**

Finally we evaluate the log likelihood to see how good our model is. Basically what is says is that the higher the result is the more sure we are that the mixture we have created fits the dataset. We plug some of the gaussian parameters into the formula, and we look the maximum value possible we can get from our distribution.


### **Pros and Cons**

#### **Advantages**
* Soft clustering
* Cluster shape flexibility

#### **Disadvantages**
* Sensitive to initialization values
* Possible to converge to a local optimum
* Slow convergence rate

## ** Some cool links**

https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.681.3152&rep=rep1&type=pdf

http://www.ai.mit.edu/projects/vsam/Publications/stauffer_cvpr98_track.pdf

## **Resources**

[Python Machine Learning Second Edition](https://www.amazon.com/Python-Machine-Learning-scikit-learn-TensorFlow/dp/1787125939)

[Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)