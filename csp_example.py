from csp.contraints import *
from input.words import *
from csp.problem import CSP
from csp.backtracking import BackTracking


class LetterConstraint(UnaryConstraint):

    def __init__(self, variable, letter, position):
        super(LetterConstraint, self).__init__(variable)
        self.letter = letter
        self.position = position

    def check(self, state):
        if self.variable in state:
            word = state[self.variable]
            if len(word) > self.position:
                return word[self.position] == self.letter
            else:
                return False
        else:
            return True


variables = ['word1', 'word2']
domains = {'word1': [w.lower() for w in words if len(w) == 6],
           'word2': [w.lower() for w in words if len(w) == 3]}
c1 = LetterConstraint('word1', 'l', 4)
c2 = LetterConstraint('word2', 'r', 0)

problem = CSP(variables=variables, domains=domains, constraints=[c1, c2])
search = BackTracking(problem=problem)
initial_state = {}
s = search.run(initial_state)
print(s)
