from dqn.dqnAgent import DQNAgent
from dqn.model import Model
import matplotlib.pyplot as plt
from tqdm import tqdm


class Train:
  def __init__(self, env, episodes, k_frames = 4):

    self.agent = DQNAgent(k_frames)
    self.episodes = episodes
    self.env = env
    self.rewards = []

  def train(self, learn=True, render=False):
    progress_bar = tqdm(range(self.episodes))

    for e in progress_bar:
      # reset state at the beggining of each game
      state = self.env.reset()    
      state = Model.frames_preprocessing(state)
      
      total_reward = 0

      while(True):
          if render: self.env.render()
          
          action = self.agent.act(state)
          next_state, reward, done, info = self.env.step(action)
          next_state = Model.frames_preprocessing(next_state)
          
          self.agent.memory.add(state, action, reward, next_state, done)
          
          state = next_state
          
          total_reward += reward
          
          if done:
              progress_bar.set_description("episode: {}, score: {}".format(e + 1, total_reward))
              self.rewards.append(total_reward)
              break
        
      if render: self.env.close()
      
      if learn:
        # train the agent with the experience of the episode
        self.agent.learn()

  def plot_rewards(self):
    if len(self.rewards) == 0:
      print("Please run the 'train' function to add some rewards")
      return

    plt.plot(self.rewards)
    plt.title("Total Reward over all episodes")
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.show()