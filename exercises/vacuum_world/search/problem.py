import math

import numpy as np


class VacuumState:
    def __init__(self, env, vacuum_position):
        self.env = env
        self.vacuum_position = vacuum_position


class VacuumProblem:

    def __init__(self, initial_state, goal_state, vacuum_position):
        self.initial_state = VacuumState(env=initial_state,
                                         vacuum_position=vacuum_position)
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

    def cost(self, state: VacuumState, action):
        """
        Given a state and an action return the cost of the action
        :param state: a state
        :param action: a possible action
        :return: a cost
        """
        return 1

    def h(self, state: VacuumState):
        """
        Given a state return the value of the heuristic
        :param state: a state
        :return: the heuristic value
        """
        # this heuristic measure the number of dirty square
        h = sum([el for el in state.env])
        return h

    @staticmethod
    def print(state):
        n = int(math.sqrt(len(state)))
        print(f'{np.array(state).reshape((n, n))}')
