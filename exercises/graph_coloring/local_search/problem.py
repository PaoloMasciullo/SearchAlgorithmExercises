import random


class GraphColoringProblem:

    def __init__(self, initial_state, nodes, colors, map_adjacent_nodes):
        self.initial_state = initial_state
        self.nodes = nodes
        self.colors = colors
        self.map_adjacent_nodes = map_adjacent_nodes

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
        An action is a tuple (key, value) in which key is the name of the region to color and value is the color to use
        example: ('WA', 'r')
        :param state: actual state
        :return: a list of actions
        """
        possible_action = [(node, color) for node in self.nodes for color in self.colors]
        random.shuffle(possible_action)
        return possible_action

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        new_state = dict(state)
        new_state[action[0]] = action[1]
        return new_state

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return len(state) == len(self.nodes) and self.conflicts(state) == 0

    def cost(self, state, action):
        """
        Given a state and an action returns the cost of the action
        :param state: a state
        :param action: an action
        :return: the cost of doing that action in that state
        """
        return 1

    def conflicts(self, state):
        conflicts = 0
        for node in state.keys():
            adjacent_nodes = [n for n in self.map_adjacent_nodes[node] if n in state.keys()]
            conflicts += sum([1 for n in adjacent_nodes if state[node] == state[n]])
        return conflicts / 2

    def value(self, state):
        return len(state) - self.conflicts(state)
