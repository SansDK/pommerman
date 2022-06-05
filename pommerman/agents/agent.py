"""
Twygger AI agent
Mark de Jong - Ken van Grinsven
"""
from pommerman.agents import BaseAgent
import pommerman.characters as characters
import pommerman.constants as constants
import gym
import random
from tensorforce.agents import Agent


class TwAIgerAgent(BaseAgent):
    directions = [
        constants.Action.Right,
        constants.Action.Left,
        constants.Action.Up,
        constants.Action.Down,
    ]

    def initialize(self, env):
        env = gym.make('PommeFFACompetition-v0')
        states = dict(type='float', shape=env.observation_space.shape)
        actions = dict(type='int', num_actions=env.action_space.n)
        return Agent.create(
            agent='dqn', environment=env, batch_size=10, learning_rate=1e-3,
            states=states, actions=actions
        )

    def __init__(self, character=characters.Bomber, algorithm='ppo'):
        super(TwAIgerAgent, self).__init__(character)
        self.algorithm = algorithm

    def create_model(self, model):
        env = gym.make('PommeFFACompetition-v0')
        agent = Agent.create(
            agent='dqn', environment=env, batch_size=10, learning_rate=1e-3
        )

        # model = Sequential()
        # model.add(Flatten(input_shape=(1, env.observation_space.shape[0])))
        # model.add(Dense(24, activation='relu'))
        # model.add(Dense(24, activation='relu'))
        # model.add(Dense(actions, activation='linear'))

        # policy = BoltzmannQPolicy()
        # memory = SequentialMemory(limit=50000, window_length=1)
        # dqn = DQNAgent(model=model, memory=memory, policy=policy,
        #             nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
        # dqn.compile(Adam(lr=1e-3), metrics=['mae'])
        # dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)
        # _ = dqn.test(env, nb_episodes=5, visualize=True)

    def act(self, obs, action_space):

        return random.choice(self.directions).value

    # def episode_end(self, reward):
