# **Monte Carlo Methods**

Unlike dynamic programming, Monte Carlo methods uses an average of state-values (or state-action-values) from different episodes to build its value function and policy. MC methods don't know the one step dynamics before hand.

In the black jack example, the agent can decide to hit or stick based on experience, given a state, but she doesn't know what the next state or reward will be.

![optimal policy for black jack game](/images/rl_black_jack_policy.png)

## **MC Prediction: State Values**

* Finds the value function (or action value function) corresponding to a policy π.
* Methods that evaulate a policy π from interaction with the environment fall one of two categories:
  * **On-policy** methods have the agent interact with the environment by following the same policy π that it seeks to evaluate (or improve).
  * **Off-policy** methods have the agent interact with the environment by following a policy _b_ that is different from the policy that it seeks to evaluate (or improve).
* Each occurrence of state s ∈ S in an episode is called a visit to s.
  * **First visit MC** estimates the state value as the average of the returns following only first visits to s (it ignores the returns of following visits in an episode).
  * **Every-visit MC** estimates the state value as the average of the returns of all the visits to a state s.

  ![mc state values pseudocode](/images/rl_mc_pred_state.png)

## **MC Prediction: Action Values**

* Finds the action value function corresponding to a policy π.
* Each occurrence of the state-action pair s,a (s∈S, a∈A) in an episode is called a visit to s,a.
  * **First visit MC** estimates the action-value function following a policy π as the average of the returns following only first visits to s,a.
  * **Every visit MC** estimates the action-value function following a policy π as the average of the returns of all visits to s,a.

  ![mc action value pseudocode](/images/rl_mc_pred_action_val.png)


-----

## **Generalized policy iteration**

**Generalized policy iteration (GPI)** refers to the method of alternating rounds of policy evaluation and policy improvement in the search for an optimal policy. 

## **MC Control: Incremental Mean and Policy Evaluation**

* A method for updating a state value after every episode of interaction.
* Every update has the same weight. 

![incremental mean](/images/rl_incremental_mean.png)

<sub>
x = expected_return, mu = current_state_value
</sub>


## **MC Control: Policy Improvement**

* A policy is **greedy** with respect to an action-value function Q if for every state s∈S it selects the action with that will return the highest state-value.
* A policy is **ϵ-greedy** with respect to an action value function Q if for every state s∈S it selects: 
  * the greedy action with probability 1 - ϵ.
  * a random action with probability ϵ.

-----

## **Exploration vs. Exploitation**

* All reinforcement learning agents face the **Exploration-Exploitation Dilemma**, where they must find a way to balance the drive to behave optimally based on their current knowledge (**exploitation**) and the need to acquire knowledge to attain better judgement (**exploration**).
* In order for MC control to converge to the optimal policy, the **Greedy in the Limit with Infinite Exploration (GLIE)** conditions must be met:
  * evey state-action pair s,a (for all s∈S and a∈A(s)) is visited infinitely many times, and
  * the policy converges to a policy that is greedy with respect to the action-value function estimate Q.

![exploration vs. Exploitation GLIE](/images/rl_mc_control_exploration.png)

## **MC Control: Constant alpha**

* A constant alpha instead of the running mean helps the agent forget about the policies followed in the past, and give more importance to policies followed recently where he has more experience.
* The step-size parameter α must satisfy 0 < α ≤ 1. Higher values of alpha will result in faster learning (it uses less information about past experience), but values of alpha that are too high can prevent MC control from converging to the optimal policy.

![contant alpha update](/images/rl_mc_constant_alpha.png)



![alternative update step](/images/rl_update_action_value_function.png)

<sub>(UP) Alternative way of writing the update step</sub>
