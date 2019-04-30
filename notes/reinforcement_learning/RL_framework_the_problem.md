# **The RL Framework: The Problem**

![agent environment interaction](/images/rl_agent_env_interaction.png)

## **The Setting, Revisited**

* The Reinforcement Learning Framework is characterized by an **agent** learning to interact with its **environment**.
* At each time step **_t_** the agent recieves a **state** from the environment and must choose an **action** to take in response. One time step later **_t + 1_** the agent recieves a **reward** and a new state.
* The agent's goal is to maximize **cumulative reward**, or reward obtained over all time steps.


## **Episodic vs. Continuing Tasks**

* A **task** is an instance of the RL problem, eg: picking up trash in the robot example.
* **Continuing tasks** are tasks that continue forever without end.
* **Episodic tasks** have a well defined starting and ending point.
  * A complete sequence of interaction, from start to finish, is an **episode**.
  * Episodic tasks come to an end when the agent reachese a **terminal state**.

## **Reward hypothesis**

* **Reward hypthesis** All goals can be framed as the maximization of (expected) cumulative reward.

## **Goals and Rewards**

* How we specify the **reward** will depend on the problem we are trying to solve.


## **Cumulative Reward**

* The **return at a time step** *t* is *G<sub>t</sub> = R<sub>t+1</sub> + R<sub>t+2</sub> + R<sub>t+3</sub> +  ...* .

* The **agent** selects actions that maximize the expected cumulative return.

## **Discounted Return**

* The **Discounted Return** at a time step *t* is *G<sub>t</sub> = R<sub>t+1</sub> + γR<sub>t+2</sub> + γ<sup>2</sup>R<sub>t+3</sub> +  ...*
* The discount rate γ is a hyperparameter to refine the goal of the agent.
  * It must satisfy 0 ≤ γ ≤ 1.
  * If γ = 0, the agent only cares about the most immediate reward.
  * If γ = 1, the return is not discounted.
  * For larger values of γ, the agent cares more about the distant future. For smaller values of γ the agent cares more about the most immediate reward.

## **MDPs and One-Step Dynamics**

* The **state space *S*** is the set of all (*nonterminal*) states.
* The **state space *S***<sup> +</sup> is the set of all states including the terminal states.
* The **Action space *A*** is the set of all possible actions. (Alternatively ***A***( *s* ) refers to all the possible actions given a state *s* ∈ ***S*** ) .
* The **one-step dynamics** of the environment decide the state and reward for each time step. They can be defined as: ![one step dynamics formula](/images/rl_one_step_dynamics.png) for each possible *s', r, s* and *a*.
* A **(finite) Makrov Decision Process** is defined by:
  * a (finite) set of states ***S*** (or ***S***<sup> +</sup> for an episodic task).
  * a (finite) set of actions ***A***.
  * a set of rewards ***R***.
  * the one-step dynamics of the environment.
  * the discount rate γ ∈ [0,1].