# **Discretization**

Discretization is the process of converting a continous space into a dicrete space so that we can perform our reinforcement learning algorithms.

## **Uniform Grid Discretization**

**Uniform Grid Discretization** consists of converting a continous space into a grid space. After having created the grid, any continous value gets converted into a discrete value equal to the grid point where this value is located.

The bigger the grid is, the more precision the value function will have with the cost of being more computationally expensive.

![discretization](/images/discretization.png)

Now that we  have a way of converting a continous space into a discrete space, we can use our RL Algorithms.

## **Tile Coding**

**Tile Coding** consists of overlaying multiple grids or tilings on top of the state space, each slightly offset from each other. Every state in the state space can be identified by the tiles where it can be found.

![tile coding example](/images/rl_tile_coding_ex.png)

![tile coding algorithm](/images/rl_tile_coding.png)

