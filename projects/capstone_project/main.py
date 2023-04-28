import gym
from baselines.common.atari_wrappers import MaxAndSkipEnv, NoopResetEnv, wrap_deepmind
from dqn.dqnAgent import DQNAgent
from dqn.train import Train
from gym.wrappers.atari_preprocessing import AtariPreprocessing

if __name__ == "__main__":

    env = gym.make('SpaceInvaders-v0')
    env = NoopResetEnv(env)
    env = MaxAndSkipEnv(env)
    env = wrap_deepmind(env, episode_life=False, clip_rewards=True, frame_stack=True, scale=False)

    episodes_train = 100
    agent_train = DQNAgent(dueling=True)

    train = Train(env, agent_train)
    # Train the agent
    train.train(episodes_train, learn=False, render=False, monitor=False)
    # Plot the rewards
    train.plot_rewards()
