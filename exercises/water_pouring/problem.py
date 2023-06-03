import numpy as np


class WaterPouring:
    def __init__(self, initial_state, goal_state, jugs_capacity):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.jugs_capacity = jugs_capacity

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
        possible_actions = []
        fills = [('Fill', i) for i in range(len(state)) if state[i] < self.jugs_capacity[i]]
        possible_actions.extend(fills)
        dumps = [('Dump', i) for i in range(len(state)) if state[i] > 0]
        possible_actions.extend(dumps)
        pours = [('Pour', i, j) for i in range(len(state)) for j in range(len(state)) if
                 state[i] > 0 and state[j] < self.jugs_capacity[j] and i != j]
        possible_actions.extend(pours)
        return possible_actions

    def fill(self, state, i):
        new_state = list(state)
        new_state[i] = self.jugs_capacity[i]
        return tuple(new_state)

    def dump(self, state, i):
        new_state = list(state)
        new_state[i] = 0
        return tuple(new_state)

    def pour(self, state, i, j):
        new_state = list(state)
        jug_i = new_state[i]
        jug_j = new_state[j]

        delta_j = self.jugs_capacity[j] - jug_j

        if delta_j >= jug_i:
            jug_j += jug_i
            jug_i = 0
        else:
            jug_i -= delta_j
            jug_j += delta_j

        new_state[i] = jug_i
        new_state[j] = jug_j
        return tuple(new_state)

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        if action[0] == 'Fill':
            return self.fill(state, action[1])
        if action[0] == 'Dump':
            return self.dump(state, action[1])
        if action[0] == 'Pour':
            return self.pour(state, action[1], action[2])

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        for jug in state:
            if jug == 4:
                return True
        return False

    def cost(self, state, action):
        """
        Given a state and an action returns the cost of the action
        :param state: a state
        :param action: an action
        :return: the cost of doing that action in that state
        """
        if action[0] == 'Fill':
            return self.jugs_capacity[action[1]] - state[action[1]]  # the amount of water used
        return 0

    def h(self, state):
        h = min(state, key=lambda jug: - abs(jug - self.goal_state))
        return h
