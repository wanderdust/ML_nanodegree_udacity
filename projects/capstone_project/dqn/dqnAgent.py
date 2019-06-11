from dqn.replayBuffer import ReplayBuffer
from dqn.model import Model
import numpy as np

class DQNAgent:
  def __init__(self, env):

    # Hyperparameters
    self.learning_rate = 0.01
    self.gamma = 0.95 # discount rate
    self.epsilon = 1 # exploration
    self.epsilon_decay = 0.995
    self.epsilon_min = 0.001
    
    # Model
    self.state_size = (80,80,2)
    self.action_size = 6
    self.model = Model(self.state_size, self.action_size, self.learning_rate).model

    # Model with fixed weights w-
    self.model_f = Model(self.state_size, self.action_size, self.learning_rate).model
    self.c_steps = 10 # how often w- gets updated
    self.c_steps_counter = 0

    # Replay memory
    self.buffer_size = 100000
    self.batch_size = 64
    self.memory = ReplayBuffer(self.buffer_size, self.batch_size)

  def act(self, state):
    """
    Choose action using greedy policy
    """
    if np.random.rand() <= self.epsilon:
      # select random action
      return np.random.choice(np.arange(self.action_size))

    # select greedy action
    act_values = self.model.predict(state)
    return np.argmax(act_values[0])


  def sample(self, state):
    """
    1. Choose action A from state S 
    2. Take action A, observe reward R and next S
    3. Prepare next state S'
    4. Store experience tuple (S,A,R,S') in replay memory
    5. S <- S'
    """
    pass

  def update_model_f(self):
    """
    Updates fixed weights of the 'model_f' every C steps.
    """
    if self.c_steps_counter == self.c_steps:
      self.model_f.set_weights(self.model.get_weights()) 
      self.c_steps_counter = 0
    else:
      self.c_steps_counter += 1

  def learn(self, batch_size=32):
    """
    1. Obtain a batch of random samples
    2. Set target y = r + gamma*max q(s,a,w-)
    3. Update weights (forward pass -> Gradient descent)
    4. Update fixed w after C steps w- <- w
    """
    minibatch = self.memory.sample(batch_size)
    
    for state, action, reward, next_state, done in minibatch:
      target = reward
      if not done:
        target = reward + self.gamma * np.amax(self.model_f.predict(next_state)[0])

      # Convert target to have the same shape as output
      target_f = self.model.predict(state)
      target_f[0][action] = target

      self.model.fit(state, target_f, epochs=1, verbose=0)
      self.update_model_f()

    if self.epsilon > self.epsilon_min:
      self.epsilon *= self.epsilon_decay


  