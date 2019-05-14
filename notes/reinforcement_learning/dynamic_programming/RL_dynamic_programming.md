# **Dynamic Programming**

## **What is dynamic Programming**

In the **dynamic programming** setting, the agent has full knowledge of the one-step dynamics of the environment. This makes it much easier than the **Reinforcement Learning** setting where the agent has no prior knowledge of how the environment decides the state and reward, and must learn from interaction how to select actions. 


## **Using a system of equations to get the state-values**

One method to get the state values of the environment given a policy is to solve a system of bellman's equation for all states. However we will focus in the iterative method approach.

![system of bellman equations](/images/rl_system_of_equations.png)


## **Iterative Policy Evaluation**

* Algorithm used in the dynamic setting to estimate the state value function v<sub>π</sub> corresponding to a policy π.
* We update the state values until the increase of the state values is very little (delta < theta).

![iterative policy evaluation](/images/rl_iterative_policy_evaluation.png)


## **Action values**

* The action value is the state value that a state would have if the agent takes a specific action, and then follows the policy for the rest of the episode.
* We can calculate the action values for each state using bellman's equation.

![state action values](/images/rl_action_values.png)

## **Policy Improvement**

* Consists on choosing the action that will give us the highest value for each state in the action-value function.
  * In the **deterministic setting** we choose only the action with the highest state-value, assigning the other actions 0% probability of ocurring.
  * In the **stochastic setting** we give the action with the highest state-value a higher probablity of occurring, assigning the other actions a lesser probability of occurring.

## **Policy Iteration**

* Consists on going through the whole process until we have an optimal policy.
* This algorithm can solve the MDP in the dynamic programming setting.

![policy iteration](/images/rl_policy_iteration.png)

-----

## **Truncated Policy Iteration**

* An alternative method to policy iteration.
* With this algorithm **the evaluation process is stopeed after fixed number of iterations**. 
* This algorithm is useful because we don't always need the most optimal state value function to obtain an optmial policy. Sometimes we can obtain the optimal policy after a few iterations, making this algorithm more efficient.

![truncated policy evaluation](/images/rl_truncated_policy_evaluation.png)

![truncated policy iteration](/images/rl_truncated_policy_iteration.png)

-----

## **Value Iteration**

* This algorithm estimates the value function v<sub>π</sub> corresponding to a policy π. In this approach, each sweep over the state space simultaneously performs policy evaluation and policy improvement.
* We only do policy evaluation once per sweep, unlike **iterative policy evaluation** or **truncated policy evaluation**.

![value iteration](/images/rl_value_iteration.png)