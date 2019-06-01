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

*Experience replay saves the experiences in a [finite] replay buffer, and then trains the network (state fucntion) at once.*

**Fixed Target**: Currently the update function updates the weights using its own value of the weights, which is mathematically incorrect, but seems to work. A better way to implement this algorithm would be to fix the value of **_w<sup>-<sup>_** which we don't change during the learning step. In practice we copy _w_ into _w<sup>-<sup>_, use it to generate targets while changing _w_ for a certain number of learning steps. Then we update the value of _w<sup>-<sup>_ to the value of  _w_, learn for a number of steps and so on.

This helps decouple the parameters.

**THE DEEP Q-LEARNING ALGORITHM**

This algorithm has 2 steps:
* The first step samples the environment by performing actions and storing away the experienced tuples in a replay memory
* The other step is where we select a small batch of tuples from the memory randomly and use the gradient descent step to learn.

These 2 processes are not directly dependent on each other, so you could sample for a number of times and then do one learning step, or even multiple learning steps with different random batches.

![Q-learning algorithm](/images/rl_q-learning_algorithm.png)

**Improvements**:
1. **Double Q-Learning**: The problem comes from choosing the state value with the max value at the early stages, because these can be noisy values. Double Q-Learning chooses the best action with some set of parameters _w_ but then evaluates that action with a set of parameters _w'_.

![Double Q-Learning](/images/q_learning_improvement_1.png)

2. **Prioritized Experience Replay**: The problem comes from having a limited replay buffer, where some important memories (eg. rare memories that don't occur often) might get lost. Prioritized experience replay uses _delta_ error function to assign priorities to each tuple: the bigger the error the more we expect to learn from that tuple. We store this error alongide each tuple in the replay buffer.

![prioritized experience replay](/images/q_learning_per.png)

3. **Dueling Networks** : The idea is to use 2 streams: one that estimates the state values, and the other to estimate the advantage values. Finally the desired Q values are obtained from combining both.

![Dueling Networks](/images/q_learning_dueling_networks.png)
*******
## **Useful Resources**

[Human-level control through deep reinforcement
learning](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)

[Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification](https://arxiv.org/abs/1502.01852)

[Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461)

[Prioritized Experience Replay](https://arxiv.org/abs/1511.05952)

[Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581)

[Deep Recurrent Q-Learning for Partially Observable MDPs](https://arxiv.org/abs/1507.06527)

[Issues in Using Function Approximation for Reinforcement Learning (1993)](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.73.3097)

**Deep learning implementations**

[Implementing Deep Q-learning with keras](https://keon.io/deep-q-learning/)

[Implementing Deep Q-learning with pytorch](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)