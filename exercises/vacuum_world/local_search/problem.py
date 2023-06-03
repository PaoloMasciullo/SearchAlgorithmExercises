import math
import random

import numpy as np


class VacuumState:
    def __init__(self, env, vacuum_position):
        self.env = env
        self.vacuum_position = vacuum_position


class VacuumProblem:
    def __init__(self, initial_state, vacuum_position, goal_state):
        self.initial_state = VacuumState(env=initial_state, vacuum_position=vacuum_position)
        self.goal_state = goal_state

    def successors(self, state: VacuumState):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state: VacuumState):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """
        n = int(math.sqrt(len(state.env)))
        actions = []
        row, col = state.vacuum_position
        new_pos = row * n + col

        if row > 0:
            actions.append('Up')
        if row < n - 1:
            actions.append('Down')
        if col < n - 1:
            actions.append('Right')
        if col > 0:
            actions.append('Left')
        if state.env[new_pos] == 1:
            actions.append('Suck')
        return actions

    def result(self, state: VacuumState, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        n = int(math.sqrt(len(state.env)))
        row, col = state.vacuum_position
        new_row = row
        new_col = col

        new_env = list(state.env)

        if action == 'Up':
            new_row = row - 1
        if action == 'Down':
            new_row = row + 1
        if action == 'Left':
            new_col = col - 1
        if action == 'Right':
            new_col = col + 1
        if action == 'Suck':
            new_pos = new_row * n + new_col
            new_env[new_pos] = 0

        return VacuumState(env=tuple(new_env), vacuum_position=tuple((new_row, new_col)))

    def goal_test(self, state: VacuumState):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return state.env == self.goal_state

    def cost(self, state, action):
        """
        Returns the cost of an action. In this problem the cost is always unitary.
        :param state: a state
        :param action: an action
        :return: a cost
        """
        return 1

    def value(self, state: VacuumState):
        """
        Returns the value of a state. This function is used for evaluating a state in the local_search search.
        (The higher the better)
        :param state: a state
        :return: the value of a state
        """
        # this function measure the number of clean square
        if isinstance(state, tuple):
            h = sum([1 for el in state if el == 0])
        elif isinstance(state, object):
            h = sum([1 for el in state.env if el == 0])
        else:
            raise TypeError
        return h

    @staticmethod
    def random(n):
        """
        Generate a random environment with n squares
        :return: a tuple with n elements
        """
        env = np.random.randint(low=0, high=2, size=(n, n)).flatten()
        return tuple(env)
