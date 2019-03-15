# **PCA (Principal Component Analysis)**

This is a technique used for feature extraction. Using PCA does not only improve storage space and computational efficiency of the learning algorithm, but also can improve the predictive performance by reducing the curse of dimensionality.

## **What is PCA**

PCA is an unsupervised lenear transformation technique used for feature extraction and dimensionality reduction. PCA helps us identify patterns in data based on correlation between features. In a nutshell, PCA finds the direction of the maximum variance in high-dimensional data and projects it into a new subspace with equal or fewer dimensions than the original one.

![PCA example](/images/pca_example1.png)

In the above image, *x<sub>1</sub>* and *x<sub>2<sub>* are the orignal axes, and PC1 and PC2 are the principal components.

## **When to use PCA**

* Find latent features driving the patterns in data
* Dimensionality reduction:
  * Visualize high-dimensional data → It reduces it to two dimensions so we can visualize it with matplotlib.
  * Reduce Noise, as it finds the patterns in the data getting rid of noise data.
  * Pre-processing for using with other algorithms.

## **Steps for Calculating PCA: High level overview**

1. Find a new coordinate system by transformation and rotation only. The center of the new coordinate system (0,0) will be at the center of the data.
2. Find the new x axis in the direction of the maximum variance (variance measures how tightly coupled points are).
3. Finds a new y axis in the orthogonal, less important direction of variation.

PCA in scikit learn will return an importance vector, a spread value for the axis. It will be large for the first Principal Component, and it will be smaller for the next orthogonal axis, and so on.

## **PCA for feature transformation**

PCA will find Principal Component (new axis) by maximizing the variance. Then it will project all the features into the new PC, reducing for example from 2 dimensions into 1 dimension.

![PCA example](/images/pca_example2.png)

Information loss is the distance between the point and the Principal Component.

## **PCA Review/Definition**

* Systemized way to transform input features into principal components.
* Use principal components as new features (Note that a PCA with the same number PC as original features will be the exact same data except that it is represented in a different way).
* Principal Components are directions in data that maximize variance (minimize information loss) when you project/compress down onto them.
* The more variance of data along a PC, the higher the PC is ranked.
* The first PC will have the most variance/information; the second one will have the second most variance/information and so on. All PC are orthogonal to each other, which means they will never overlap.
* Max number of Principal Components = Number of input features.

## **Resources**

[Python Machine Learning Second Edition](https://www.amazon.com/Python-Machine-Learning-scikit-learn-TensorFlow/dp/1787125939)

[Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)