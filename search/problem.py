import math
import random

import numpy as np


class StreetProblem:

    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """
        return self.environment.streets[state]

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        return action

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return state == self.goal_state

    def cost(self, state, action):
        """
        Given a state and an action returns the cost of the action
        :param state: a state
        :param action: an action
        :return: the cost of doing that action in that state
        """
        reached_state = self.result(state, action)
        return self.environment.distance(state, reached_state)

    def h(self, state):
        goal_x, goal_y = self.environment.coordinates[self.goal_state]
        x, y = self.environment.coordinates[state]
        return math.sqrt((goal_x - x) ** 2 + (goal_y - y) ** 2)


class EightTilesProblem:

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def get_empty_tile(self, state):
        """
        Given a state returns the column and the row of the empty tile in the puzzle
        :param state: a state
        :return: a row and a column
        """
        pos = state.index(0)
        row = pos // 3
        col = pos % 3
        return row, col

    def actions(self, state):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """
        actions = []
        row, col = self.get_empty_tile(state)
        if row > 0:
            actions.append('Up')
        if row < 2:
            actions.append('Down')
        if col < 2:
            actions.append('Right')
        if col > 0:
            actions.append('Left')
        return actions

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        row, col = self.get_empty_tile(state)
        new_row = row
        new_col = col

        if action == 'Up':
            new_row = row - 1
        if action == 'Down':
            new_row = row + 1
        if action == 'Left':
            new_col = col - 1
        if action == 'Right':
            new_col = col + 1

        new_pos = new_row * 3 + new_col
        old_pos = row * 3 + col
        new_state = list(state)
        new_state[old_pos] = state[new_pos]
        new_state[new_pos] = 0

        return tuple(new_state)

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return state == self.goal_state

    def cost(self, state, action):
        """
        Given a state and an action return the cost of the action
        :param state: a state
        :param action: a possible action
        :return: a cost
        """
        return 1

    def h(self, state):
        """
        Given a state return the value of the heuristic
        :param state: a state
        :return: the heuristic value
        """
        h = 0
        for index in range(8):
            if state[index] != self.goal_state[index]:
                h += 1
        return h

    @staticmethod
    def print(state):
        print('_____________')
        for i, n in enumerate(state):
            print('|', end='')
            if n == 0:
                n = 'x'
            print(f' {n} ', end='')
            if i % 3 == 2:
                print('|')
        print('_____________')


class EightQueensProblem:

    def __init__(self, initial_state=None):
        if initial_state is None:
            initial_state = self.random()
        self.initial_state = initial_state
        self.max_conflicts = sum([i for i in range(1, 8)])

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """
        actions = []
        for col, queen in enumerate(state):
            squares = list(range(0, 8))
            squares.remove(queen)
            new_actions = list(zip(squares, [col] * len(squares)))
            actions.extend(new_actions)
        return actions

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        new_state = list(state)
        col, new_row = action
        new_state[col] = new_row
        return tuple(new_state)

    def conflicts(self, state):
        """
        Given a state return the number of conflicts
        :param state: a state
        :return: number of conflicting queens
        """
        conflicts = 0
        for col in range(8):
            queen = state[col]
            for col1 in range(col + 1, 8):
                queen1 = state[col1]

                if queen == queen1:
                    conflicts += 1
                if queen - col == queen1 - col1 or queen + col == queen1 + col1:
                    conflicts += 1
        return conflicts

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return self.conflicts(state) == 0

    def cost(self, state, action):
        """
        Returns the cost of an action. In this problem the cost is always unitary.
        :param state: a state
        :param action: an action
        :return: a cost
        """
        return 1

    def value(self, state):
        """
        Returns the value of a state. This function is used for evaluating a state in the local_search search.
        (The higher the better)
        :param state: a state
        :return: the value of a state
        """
        return self.max_conflicts - self.conflicts(state)

    @staticmethod
    def random():
        """
        Generate a random chess with 8 queens
        :return: a tuple with 8 elements
        """
        chess = [random.randrange(0, 8) for _ in range(8)]
        return tuple(chess)

    @staticmethod
    def print_chess(state):
        print('\t', end='')
        for number in [1, 2, 3, 4, 5, 6, 7, 8]:
            print(f"|  {number}  ", end='')
        print('|', end='')
        print('\n\t_________________________________________________')

        for row, letter in zip(range(8), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
            print(letter + '\t', end='')
            print('|', end='')

            for queen in state:
                if queen == row:
                    print('  Q  ', end='')
                else:
                    print('     ', end='')
                print('|', end='')
            print('\n', end='')
            print('\t_________________________________________________')


