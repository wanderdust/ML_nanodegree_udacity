import numpy as np
from dqn.model import Model
import matplotlib.pyplot as plt
from tqdm import tqdm
from gym.wrappers import Monitor
from time import time

class Train:
  def __init__(self, env, agent):

    self.agent = agent
    self.env = env
    self.rewards = []

  def train(self, episodes, learn=True, render=False, monitor=False):

    # Record video
    # Records only the first episode
    if monitor:
      self.env = Monitor(self.env, './videos/' + time() + '/', resume=True)

    progress_bar = tqdm(range(episodes))

    for e in progress_bar:
      # reset state at the beggining of each game
      state = self.env.reset()    
      state = Model.state_to_tensor(state)

      total_reward = 0

      while(True):
          if render: self.env.render()
          
          action = self.agent.act(state)
          next_state, reward, done, info = self.env.step(action)
          next_state = Model.state_to_tensor(next_state)
          
          self.agent.memory.add(state, action, reward, next_state, done)
          
          state = next_state
          
          total_reward += reward
          
          if done:
              progress_bar.set_description(" score: {}".format(total_reward))
              self.rewards.append(total_reward)
              break
        
      if render or monitor: self.env.close()
      
      if learn:
        # train the agent with the experience of the episode
        self.agent.learn()

      # Save model weights evey n episodes
      if learn and e % 1000 == 0:
        self.agent.save_weights('best_model')
        progress_bar.set_description("Saving the model")

      # Save the model on the last episode as well.
      if e == episodes:
        self.agent.save_weights('best_model')
        progress_bar.set_description("Saving the model")

  def plot_rewards(self):
    if len(self.rewards) == 0:
      print("Please run the 'train' function to add some rewards")
      return

    avg_score = np.mean(self.rewards)
    print("Average score: {}".format(avg_score))
    plt.plot(self.rewards)
    plt.title("Total Reward over all episodes")
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.show()
    