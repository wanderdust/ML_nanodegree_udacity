# **Function Aproximation**

We use a function to predict a state value from a state (or a state-action). To do this we introduce a parameter value **_w_** that shapes the function (eg. The linear function can look like **v<sub>π</sub>(s, w) = s<sub>1</sub>w<sub>1</sub> + s<sub>2</sub>w<sub>2</sub>**):

![function aproximation](/images/rl_function_aprox.png)

Thus, to obtain the aproximate state value (or state-action value) we need to do the dot product of the state's vector and their weights. x(s) represents the vector version of s.

![dot product](/images/rl_dot_product.png)

-------

**Gradient descent**

We use **gradient descent** to update the weights thus finding an optimal state value function.

1. First we create the value function v<sub>π</sub>(s, w) =  s<sub>1</sub>w<sub>1</sub> + ... + s<sub>n</sub>w<sub>n</sub>

2. Build the error function, which is the squared vale of the distance from the real value.

3. Calculate the gradient with respect to the weights.

4. Update the weights.


Illustration of the mentionied above:

![gradient descent](/images/rl_gradient_descent.png)

If we wanted to know the value from an state-action input, we would simply have to construct a vector x(s,a), and perform the same steps.

![state action vector](/images/rl_state_action_vector.png)

-----


**Output all possible action value functions from input state**

![action vector output](/images/rl_action_vector.png)

We can acomplish this by multiplying the input vector by a matrix of weights, each column representing a linear function.

![](/images/rl_state_action_aprox-fn.png)

----

## **Limitations of linear function aproximation**

* We can only represent linear relations between inputs and ouptuts, which is often  not the case, getting a real bad aproximation result.

* We can use Deep Neural Networks to catch these non-linear relationships.