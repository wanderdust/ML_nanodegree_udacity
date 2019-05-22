# **Deep Q-Learning**

## **Neural Networks as Value Functions**

We can use a Neural Network to find our value for a state, or values for action states. The problem we face now is **what value we should use to compute the error function (squared distances) and update the weights**.

![Neural Network Value Function](/images/q_learning_nn_value_fn.png)


### **Monte Carlo Learning to define the error function**

In monte carlo we computed the expected reward G<sub>t</sub> and used it to update the state-values.

We can use G<sub>t</sub> to compute the error function for the neural network aproximator:

![Monte Carlo](/images/q_learning_monte_carlo.png)

**Note:** the error function above comes from doing the derivative of the squared error of the difference between G<sub>t</sub> and the predicted state-action value.

In the implementation of Every-visit Monte Carlo with the new value function as a neural network we would first update the weights (value function), followed by an improvement step where we extract an epsilon-greedy policy based on the predicted state-action values.

![Monte Carlo Algorithm](/images/q_learning_monte_carlo_algorithm.png)


### **Temporal Difference to define the error function**

In Temporal Difference we computed the discounted return for the next state and used it to update the state-values.

We can use the expected discounted return from the next state to compute the error for our neural network aproximator.

![Temporal Difference Error Function](/images/q_learning_td_error.png)

**Note:** the error function above comes from doing the derivative of the squared error of the difference between G<sub>t</sub> and the predicted state-action value.

In the Temporal Difference implementation (SARSA), we use our new update function to update the value function aproximator (the neural net).

![Q-learning Algorithm](/images/q_learning_td_algorithm.png)

We can use the same algorithm for continuing tasks by repeating the algorithm forever without stopping at a terminal state.

-------

## **Deep Q-Learning**

**Q-learning** is a type of temporal difference algorithm that falls under the category of **off-policy** because we are not using the same policy to make decisions and update the state-value function.

![Deep Q-Learning](/images/q_learning_q-learning.png)

The reason why we choose off-policy methods is because they de-couple the actions an agent takes in the environment from its learning process. This gives us the oportunity to build different variations in the learning algorithm. For example, using a more exploratory policy while acting and yet learn the optimal value function.

**EXPERIENCE REPLAY**

Consists on saving the state, reward, done tuples in a replay buffer and re-use them later to train our agent. We can sample them into batches and feed them to the network at once.

**Experience replay** can help by recalling some unusual states as well as preventing the agent to learn from unwanted sequences by shuffling the batches.

*Experience replay saves the experiences in a replay buffer, and then trains the network (state fucntion) at once.*

**Fixed Target**: Currently the update function updates the weights using its own value of the weights, which is mathematically incorrect, but seems to work. A better way to implement this algorithm would be to fix the value of **_w<sup>-<sup>_** which we don't change during the learning step. In practice we copy _w_ into _w<sup>-<sup>_, use it to generate targets while changing _w_ for a certain number of learning steps. Then we update the value of _w<sup>-<sup>_ to the value of  _w_, learn for a number of steps and so on.

This helps decouple the parameters.