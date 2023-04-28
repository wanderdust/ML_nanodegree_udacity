from time import time

import matplotlib.pyplot as plt
import numpy as np
from dqn.model import ModelVanilla
from gym.wrappers import Monitor
from tqdm import tqdm


class Train:
  def __init__(self, env, agent):

    self.agent = agent
    self.env = env
    self.rewards = []
    self.rewards_filepath = 'saved_models/rewards.txt'

    # Empty rewards file
    open(self.rewards_filepath, 'w').close()

  def train(self, episodes, learn=True, render=False, monitor=False, save_episodes=100):
    '''
    params
    ========
      learn: whether the agent performs gradient descent or not
      render: render a video of the agent performing
      monitor: record a video
      save_episodes: save the model's weight every n episodes
    '''
    # Record video
    # Records only the first episode
    if monitor:
      self.env = Monitor(self.env, './videos/' + str(time()) + '/', resume=True)

    progress_bar = tqdm(range(episodes))

    for e in progress_bar:
      # reset state at the beggining of each game
      state = self.env.reset()    
      state = ModelVanilla.state_to_tensor(state)

      total_reward = 0

      while(True):
          if render: self.env.render()
          
          action = self.agent.act(state)
          next_state, reward, done, info = self.env.step(action)
          next_state = ModelVanilla.state_to_tensor(next_state)
          
          self.agent.memory.add(state, action, reward, next_state, done)
          
          state = next_state
          
          total_reward += reward
          
          if done:
              progress_bar.set_description(" score: {}".format(total_reward))
              self.rewards.append(total_reward)
              if learn:
                self.save_reward(total_reward) # Write reward to file
              break
        
      if render or monitor: self.env.close()
      
      if learn:
        # train the agent with the experience of the episode
        self.agent.learn()

      # Save model weights evey n episodes or on the last episode
      if learn and e % save_episodes == 0 or e == episodes:
        self.agent.save_weights('vanilla')
        progress_bar.set_description("Saving the model")

  def plot_rewards(self, mean_avg=10, show=False):
    avg_rewards = []

    if len(self.rewards) == 0:
      print("Please run the 'train' function to add some rewards")
      return

    # Calculate the mean over the last n-rewards
    for i in range(1, len(self.rewards) + 1):
      if i % mean_avg == 0:
        avg = np.mean(self.rewards[i - mean_avg :i])
        avg_rewards.append(avg)

    avg_score = np.mean(self.rewards)
    print("Average score: {}".format(avg_score))

    x_axis = np.arange(mean_avg, len(self.rewards)+mean_avg, mean_avg)
    plt.plot(x_axis, avg_rewards)
    plt.title("Mean average every {} episodes".format(mean_avg))
    plt.xlabel('Episode')

    plt.ylabel('Reward')
    plt.savefig('ouptuts/rewards.png')
    if show:
      plt.show()

  # Save rewards to file
  def save_reward(self, reward):
    f = open(self.rewards_filepath, "a+")

    f.write("{},".format(reward))

    f.close()

  # Read rewards from file
  def load_rewards(self):
    self.rewards = [] # Empty existing rewards

    f = open(self.rewards_filepath, "r")

    if f.mode == "r":
      contents = f.read()

    file_data = contents.split(",")[:-1] # Delete last item, as it is an empty element

    for reward in file_data:
      self.rewards.append(float(reward))



    