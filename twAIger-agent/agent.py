"""
Twygger AI agent
Mark de Jong - Ken van Grinsven
"""
from pommerman.agents import BaseAgent
import pommerman.characters as characters
import pommerman.constants as constants
import gym
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam


class TwAIgerAgent(BaseAgent):
    directions = [
        constants.Action.Right,
        constants.Action.Left,
        constants.Action.Up,
        constants.Action.Down,
    ]
    actions = [
        constants.Action.Stop,
        constants.Action.Right,
        constants.Action.Left,
        constants.Action.Up,
        constants.Action.Down,
        constants.Action.Bomb
    ]
    states = []

    def __init__(self, character=characters.Bomber, algorithm='ppo'):
        super(TwAIgerAgent, self).__init__(character)
        self.algorithm = algorithm

    def create_model(self, model):
        model = Sequential()
        model.add(Flatten(input_shape=(1, self.states)))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.actions, activation='linear'))

    def act(self, obs, action_space):
        return random.choice(self.directions).value

    # def episode_end(self, reward):
