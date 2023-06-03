from input.roads import Roads


class BariRoadsProblem:
    def __init__(self, initial_state, goal_state, environment: Roads):
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
        In this case the action to go from city1 to city2 is called 'city2'
        :param state: actual state
        :return: a list of actions
        """
        return self.environment.streets[state]

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state.
        In this case the string representing the reached state is the same string
        representing the action to reach that state
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
        Given a state and an action return the cost of the action
        In this case the heuristic measure the straight distance between the city in the current state
        and the city in the next state
        :param state: a state
        :param action: a possible action
        :return: a cost
        """
        return self.environment.distance(start=state, end=action)

    def h(self, state):
        """
        Given a state return the value of the heuristic
        In this case the heuristic measure the straight distance between the city in the current state and
        the city in the goal state
        :param state: a state
        :return: the heuristic value
        """
        return self.environment.distance(start=state, end=self.goal_state)
