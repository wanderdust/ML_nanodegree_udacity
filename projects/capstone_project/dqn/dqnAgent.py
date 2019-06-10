from replayBuffer import ReplayBuffer
from model import Model

class DQNAgent:
  def __init__(self, env):
    # Fixed target
    self.fixed_w = None
    
    # Model
    self.state_size = env.observation_space.shape
    self.action_size = 6
    self.learning_rate = 0.01
    self.model = Model(self.state_size, self.action_size, self.learning_rate)

    # Replay memory
    self.buffer_size = 100000
    self.batch_size = 64
    self.memory = ReplayBuffer(self.buffer_size, self.batch_size)

  def act(self, state):
    """
    Choose action using greedy policy
    """
    pass

  def learn(self):
    """
    1. Obtain a batch of random samples
    2. Set target y
    3. Update weights (forward pass -> Gradient descent)
    4. Update fixed w after C steps
    """
    pass

  