# **Temporal Difference**

![cliff walking task](/images/rl_cliff_example.png)


Whereas the Monte Carlo prediction must wait until the end of an episode to update the value function, temporal-difference methods update the value after every time step.

For any fixed policy, one-step TD (or TD(0)) is guaranteed to converge to a true state-value function, as long as the step-size parameter alpha is small enough.

![temporal difference prediction](/images/rl_td_prediction.png)

## **State Action function**

Instead of updating the **value function** with the **state**, **reward** and **next state**, we update the **state-value function** using the **state**, **reward**, **next state** and **next action**.

from:

![value functino](/images/rl_td_state_fn.png)

to:

![state-value function](/images/rl_td_state_action_fn.png)


## **Sarsa(0)**

SARSA (**S**tate-**A**ction-**R**eward-**S**tate(next_state)-**A**ction(next_action)).

**Sarsa** is an on-policy TD control method. It is guaranteed to converge to the optiomal state-value function as long as the step-size parameter alpha is sufficiently small and a small epsilon is chosen to satisfy the **Greedy in the Limit with Infinite Exploration (GLIE)** conditions.

![sarsa](/images/rl_sarsa.png)


## **Sarsamax (Q-Learning)**

Instead of using the next_action chosen from the epsilon-policy to update the action-value function, we choose the action that maximizes reward. After that we use the action chosen from the epsilon-policy to make a move.

Sarsamax is known as an off-policy TD control method, because it doesn't use the same policy for updating and taking choosing actions.

![sarsamax](/images/rl_sarsa.png)

## **Expected Sarsa**

Instead of using the next_action chosen from the epsilon-policy to update the action-value function, we use the sum of all the possible states, each multiplied by the probability of choosing an action that will take us to that state.

Expected Sarsa is an on-policy TD control method. It is guaranteed to converge to the optimal action value, under the same conditions that guarantee convergence of Sarsa and Sarsamax.

## **Analyzing performance**

* On-policy TD control methods (Like Expected Sarsa and Sarsa) have better online performance than off-policy TD control methods (like Q-learning).

* Expected Sarsa generally achieves bettern performance than Sarsa.
