# **Feature Scaling**

Feature scaling is a crucial step in our preprocessing pipeline that will help some machine learning algorithms perform better. Some algorithms like Decision Trees, or Linear regression don't really get affected by feature scaling, however those are two of the very few exceptions.

There are two common approaches to features scaling: **normalization** and **standarization**.

## **Normalization**

Normalization consists of re-scaling all the features to a range [0,1]. The idea is to use the lowest value in the dataset as 0 and the largest value as 1. This is also called **min-max scaling**. 

We normalize so that we can combine different features that might originally have different ranges. If we don't normalize, features with higher ranges will always have more decision power, and that's not what we want.

![min-max scaling](/images/min_max_scaling.png)

One problem that we might encounter with normalization comes with outlier features, which can really mess up our data. If using normalization we need to make sure to clean up our data from any outliers.

## **Standarization**

Standarization is also a common technique that re-scales our values between [-1, 1]. This method can sometimes be more efficient for training our algorithms. Standarization is calculated by subtracting the mean to the point and dividing it by the standard deviation.

![standarization](/images/standarization.png)


## **Resources**

[Python Machine Learning Second Edition](https://www.amazon.com/Python-Machine-Learning-scikit-learn-TensorFlow/dp/1787125939)

[Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)


