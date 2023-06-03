import random


class JumpingFrogPuzzle:

    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

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
        # COME L'HO FATTO A CASA
        # slidesL = [(i, i + 1) for i in range(len(state)) if state[i:i + 2] == ('L', '.')]  # Slide L
        # hopL = [(i, i + 2) for i in range(len(state)) if state[i:i + 3] == ('L', 'R', '.')]  # Hop L
        # slideR = [(i + 1, i) for i in range(len(state)) if state[i:i + 2] == ('.', 'R')]  # Slide R
        # hopR = [(i + 2, i) for i in range(len(state)) if state[i:i + 3] == ('.', 'L', 'R')]  # Hop R
        # possible_actions = slidesL + hopL + slideR + hopR

        # COME L'HO FATTO ALL'ESAME
        possible_actions = []
        for i in range(len(state)):
            if state[i:i + 2] == ('L', '.') and i + 1 < len(state):
                possible_actions.append((i, i + 1))
            if state[i:i + 3] == ('L', 'R', '.') and i + 2 < len(state):
                possible_actions.append((i, i + 2))
            if state[i:i + 2] == ('.', 'R') and i + 1 < len(state):
                possible_actions.append((i + 1, i))
            if state[i:i + 3] == ('.', 'L', 'R') and i + 2 < len(state):
                possible_actions.append((i + 2, i))
        random.shuffle(possible_actions)
        return possible_actions

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        new_state = list(state)
        tmp = new_state[action[0]]
        new_state[action[0]] = new_state[action[1]]
        new_state[action[1]] = tmp
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
        Given a state and an action returns the cost of the action
        :param state: a state
        :param action: an action
        :return: the cost of doing that action in that state
        """
        return 1

    def h(self, state):
        h = sum([1 for i in range(len(state)) if state[i] != self.goal_state[i]])
        return h

    def value(self, state):
        r = sum([1 for i in range(len(state) // 2) if state[i] == 'R']) - sum(
            [1 for i in range(len(state) // 2) if state[i] == 'L'])
        l = sum([1 for i in range(len(state) // 2 + 1, len(state)) if state[i] == 'L']) - sum(
            [1 for i in range(len(state) // 2 + 1, len(state)) if state[i] == 'R'])
        return r + l
