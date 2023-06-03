import random


class CrossWord:
    def __init__(self, word_lengths, same_letters, vocabulary, initial_state=None):
        self.word_lengths = word_lengths
        self.same_letters = same_letters
        self.vocabulary = vocabulary
        if initial_state is None:
            initial_state = []
        self.initial_state = initial_state  # lo stato è una lista di parole

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        random.shuffle(possible_actions)
        return [(self.result(state, a), a) for a in possible_actions]

    def words_with_length(self, length):
        return [w.lower() for w in self.vocabulary if len(w) == length]

    def actions(self, state):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """

        if len(state) == len(self.word_lengths):
            return []

        len_next_word = self.word_lengths[len(state)]
        next_words = self.words_with_length(len_next_word)
        return next_words

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

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return len(state) == len(self.word_lengths) and self.conflicts(state) == 0

    def cost(self, state, action):
        """
        Returns the cost of an action. In this problem the cost is always unitary.
        :param state: a state
        :param action: an action
        :return: a cost
        """
        return 1

    def conflicts(self, state):
        """
        given a state count the number of conflicts. a conflict is when two words cross each other with two different letters
        @param state:
        @return:
        """
        conflicts = 0
        for w1, w2, pos1, pos2 in self.same_letters:
            if w1 in range(len(state)):
                if w2 in range(len(state)):
                    if state[w1][pos1] != state[w2][pos2]:
                        conflicts += 1
        return conflicts

    def value(self, state):
        """
        Returns the value of a state. This function is used for evaluating a state in the local_search search.
        (The higher the better)
        :param state: a state
        :return: the value of a state
        """
        # measure of how good is the state
        # number of words assigned - number of conflicts (letter that mismatch)
        return len(state) - self.conflicts(state)

    def random(self):
        random_state = []
        for i in range(len(self.word_lengths)):
            possible_words = self.words_with_length(self.word_lengths[i])
            random.shuffle(possible_words)
            random_state.append(possible_words.pop())
        return random_state
