# **The RL Framework: The Solution**

![State value function for golf example](/images/rl_state_value_function_example.png)


## **Policies**

* A **deterministic policy** is a mapping π : ***S*** → ***A***. For each state *s* ∈ ***S***, it returns the action *a* ∈ ***A*** that the agent will choose while in state *s*.

* A **stochastic policy** is a mapping π : ***S*** × ***A→***[0,1]. For each state *s* ∈ ***S*** and action *a* ∈ ***A***, it returns the probability π(*a*∣*s*) that the agent chooses an action *a* while in state *s*.

## **State-Value Functions**

* The state-value function for a policy π is denoted *v*<sub> π</sub>. For each state *s* ∈ ***S*** it yields the expected return if the agent starts in state *s* and uses the policy to choose its actions for all time steps. That is, ![](/images/rl_state_value_function.png). We refer to *v*<sub> π</sub>(*s* ) as the **value of state** *s* **under the policy** π.

* The notation E<sub>π </sub>[⋅] is the expected value of a random variable, given that the agent follows the policy π.


## **Bellman Equations**

* The **Bellman expectation equation** for  *v*<sub> π</sub> is ![bellman](/images/rl_bellman_expectation_equation.png)

## **Optimality**

* A policy π' is defined to better than or equal to a policy π if and only if *v*<sub> π'(s)</sub> ≥ *v*<sub> π(s)</sub> for all *s* ∈ ***S***.
* An **optimal policy** π<sub>\*</sub> satisfies π<sub>\*</sub> ≥ π for all policies π. An optimal policy is guaranteed to exist but may not be unique.
* All optimal policies have the same state-value function *v*<sub>\*</sub>, called the **optimal state-value function**.
 

 ## **Action-Value functions**

 * The **action-value function** for a policy π is denoted *q*<sub>π</sub>. For each state *s* ∈ ***S*** and action *a* ∈ ***A***, it yields the expected return if the agent starts in state *s*, takes action *a*, and then follows the policy for all future time steps. That is, ![](/images/rl_action_value_functions.png). We refer to *q*<sub>π</sub>(*s , a* ) as the **value of taking action** *a* **in state** *s* **under a policy** π (or alternatively as the **value of the state-action pair** *s, a*).
 * All optimal policies have the same state-action value function *q*<sub>\*</sub>, called the **optimal action-value function**

 ## Optimal Policies

 * Once the agent determines the optimal action-value function *q*<sub>\*</sub>, it can quilckly obtain an optimal policy π<sub>\*</sub> by setting ![](/images/rl_obtain_optimal_policy.png).
