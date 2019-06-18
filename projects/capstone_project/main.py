import gym
from dqn.dqnAgent import DQNAgent
from dqn.train import Train
from gym.wrappers.atari_preprocessing import AtariPreprocessing
from baselines.common.atari_wrappers import NoopResetEnv, MaxAndSkipEnv, wrap_deepmind


if __name__ == "__main__":

    env = gym.make('SpaceInvaders-v0')
    env = NoopResetEnv(env)
    env = MaxAndSkipEnv(env)
    env = wrap_deepmind(env, episode_life=False, clip_rewards=True, frame_stack=True, scale=False)

    episodes_train = 700
    agent_train = DQNAgent()

    train = Train(env, agent_train)
    # Train the agent
    train.train(episodes_train, learn=True, render=False)