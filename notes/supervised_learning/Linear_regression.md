# **Linear Regression**

Linear regression is used when we want to predict quantitative values, such as the price of a house. Linear regression is normally used when data is linear.

![](/images/linear_regresion_graph_2d.png)
![](/images/linear_regresion_graph_3d.png)

Note that linear regression doesn't need to always be linear. We can use polynomial regression, which is the same thing, except that the function has a higher degree, so it is no longer a linear function.

### **Gradient Descent**

We start by drawing a random line that fits our data, and calculate the error. The error will be the sums of the distances from the data points to the line. We minimize this error by using gradient descent.


Gradient Descent is calculated by taking the partial derivative of the error function with repect to the weights. This will give us the gradient to the fastest ascent. Because we want to reduce the error, we take the negative of the gradient. Then we multiply the gradient by the learning rate (because we want to take small steps) and update the weights.

![gradient descent formula](/images/gradient_descent_formula.png)

We apply gradient descent until we reach a local minima or the lowest error.

![gradient descent formula](/images/gd_graph.png)

### **Error Functions**

#### **Mean Absolute Error**

The mean absolute error is calculated by finding the distance from our point (x,y) to the line (the classifier) with the same x coordiante (x, y_hat). We do this for all the points and sum their absolute errors, and get the average by dividing it by the number of points.

![](/images/mean_absolute_error.png)


#### **Mean Squared Error**

The mean squared error is the average of the squared distances from the points (x, y) to the line with the same x coordinate (x, y_hat).

![](/images/mean_squared_error.png)

The only reason why we are multiplying the error by the constant *1/2* is only for convenience for calculating the derivatives with gradient descent.

The mean squared error is more useful in some cases. For example in the graph below, if we apply the mean absolute error we will get the same error for all three lines. However the squared error will give us the optimal line, which is B.

![](/images/mean_squared_error_example.png)


### **Regularization**

Useful technique to improve our models and make sure they don't overfit.

 Regularization helps us decide what to choose between a complex model (polinomial regression) and a simple model (linear regression). The way it does that is by adding the complexity of the function into the error. The complexity is calculated by the sum of the weights (w_0 + ... + w_n). After adding the complexity to the error, we choose the one with the smallest overall error.
* **L1 Regularization**: complexity is calculated by adding the absolute values of the weights.
* **L2 Regularization**: complexity is calculated by adding the squared values of the weights.
* **λ (Lambda)**: a parameter we can use to punish complexity. We want a complex model when we expect very little error, and a simpler one when there is room for experimentation and it is okay to make some mistakes. To get the error, we multiply the complexity error by lambda. A higer lambda means we will punish complexity more, and a lower lambda means we will punish simplicity more.




### **Extra notes**

![](/images/calculating_gradient_descent.png)


 ### **Resources**
 Udacity: [Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)