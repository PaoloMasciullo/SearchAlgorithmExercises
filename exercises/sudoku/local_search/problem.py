import random

n = 2  # number of rows and columns in a sub-bloc
m = 2  # number of rows and columns in the board (m^2 is the number of blocks in the board)


class Sudoku:

    def __init__(self, initial_state=None):
        if initial_state is None:
            initial_state = tuple([tuple([None for _ in range(n * m)]) for _ in range(n * m)])
        self.initial_state = initial_state

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
        An action is a tuple of integer ((row, col), val)); val is the number to put in the position (row, col)
        :param state: actual state
        :return: a list of actions
        """
        coordinates = [(row, col) for row in range(n * m) for col in range(n * m)]
        possible_values = [val for val in range(1, n * m + 1)]
        possible_actions = [(coord, val) for coord in coordinates for val in possible_values]
        # random.shuffle(possible_actions)
        return possible_actions

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        new_state = [list(state[row]) for row in range(n * m)]
        row, col = action[0]
        val = action[1]
        new_state[row][col] = val
        new_state = [tuple(new_state[row]) for row in range(n * m)]
        return tuple(new_state)

    def conflicts(self, state):
        """
        Given a state return the number of conflicts
        :param state: a state
        :return: number of conflicting queens
        """
        rows_conflicts = sum(
            [len([state[row][col] for col in range(n * m) if state[row][col]]) != len(
                set([state[row][col] for col in range(n * m) if state[row][col]])) for
             row in range(n * m)])

        cols_conflicts = sum(
            [len([state[col][row] for col in range(n * m) if state[row][col]]) != len(
                set([state[col][row] for col in range(n * m) if state[row][col]])) for
             row in range(n * m)])

        blocks_conflicts = sum(
            [len([state[row][col] for row in range(i, i + n) for col in range(j, j + n) if state[row][col]]) != len(
                set([state[row][col] for row in range(i, i + n) for col in range(j, j + n) if state[row][col]])) for i
             in range(0, n * m, n)
             for j in range(0, n * m, n)])

        return rows_conflicts + cols_conflicts + blocks_conflicts

    def empty_tiles(self, state):
        """
        count the number of empty tile (empty tile has a value of 0)
        @param state:
        @return:
        """
        return len([1 for row in range(n * m) for col in range(n * m) if state[row][col] is None])

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return self.empty_tiles(state) == 0 and self.conflicts(state) == 0

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
        state = tuple(tuple([state[i] for i in range(n * m * s, n * m * (s + 1))]) for s in range(n*m))
        worst_case = tuple([tuple([1 for _ in range(n * m)]) for _ in range(n * m)])
        return m*m + self.conflicts(worst_case) - self.empty_tiles(state) - self.conflicts(state)

    @staticmethod
    def random():
        """
        Generate a random state
        :return: a tuple with 8 elements
        """
        state = [random.randint(1, n * m) for _ in range((n * m)**2)]
        return tuple(state)
