from search.problem import *
from search.local_search import *
from input.words import *

# formulate the problem
class CrossPuzzle:

    def __init__(self, words_lengths, same_letters, vocabulary, initial_state=None):
        if initial_state is None:
            initial_state = []
        self.initial_state = initial_state
        self.words_lengths = words_lengths
        self.same_letters = same_letters
        self.vocabulary = vocabulary

    def words_with_length(self, length):
        return [w.lower() for w in self.vocabulary if len(w) == length]

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
        next_word = len(state)
        if next_word == len(self.words_lengths):
            return []
        return self.words_with_length(self.words_lengths[next_word])

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        new_state = list(state)
        new_state.append(action)
        return tuple(new_state)

    def conflicts(self, state):
        """
        Given a state return the number of conflicts
        :param state: a state
        :return: number of conflicting queens
        """
        conflicts = 0
        for w1, w2, pos1, pos2 in self.same_letters:
            if w1 in range(len(state)):
                if w2 in range(len(state)):
                    if state[w1][pos1] == state[w2][pos2]:
                        conflicts += 1
        return conflicts

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return len(state) == len(self.words_lengths)

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
        return len(state) - self.conflicts(state)

    @staticmethod
    def random():
        """
        Generate a random chess with 8 queens
        :return: a tuple with 8 elements
        """
        chess = [random.randrange(0, 8) for _ in range(8)]
        return tuple(chess)


problem = CrossPuzzle(words_lengths=[6, 7, 3],
                      same_letters=[(0, 1, 4, 1), (1, 2, 4, 0)],
                      vocabulary=words)

print()
# search algorithm
# search = HillClimbing(problem=problem)
search = SimulatedAnnealing(problem=problem, max_time=1000, lam=0.01)
# search = Genetic(problem=problem, population=50, generations=100, p_mutation=0.1, gene_pool=list(range(8)))

# run algorithm
result, state = search.run()

# display the exercises
print(result)
print(problem.value(state))
print(state)
