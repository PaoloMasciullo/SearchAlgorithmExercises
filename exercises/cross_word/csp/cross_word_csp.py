from csp.backtracking import *
from csp.contraints import Constraint
from csp.problem import CSP
from exercises.cross_word.input.words import words


class LetterConstraint(Constraint):
    def __init__(self, variables, positions):
        super(LetterConstraint, self).__init__(variables=variables)
        self.positions = positions

    def check(self, state):
        letters = []
        for i in range(len(self.variables)):
            if self.variables[i] not in state:
                return True
            else:
                word = state[self.variables[i]]
                letters.append(word[self.positions[i]])
        return len(set(letters)) == 1


map_variables = ['w1', 'w2', 'w3', 'w4', 'w5', 'w6']
lengths = [6, 7, 9, 5, 3, 4]

domains = {}
for i in range(len(map_variables)):
    domains[map_variables[i]] = [w.lower() for w in words if len(w) == lengths[i]]

c1 = LetterConstraint(variables=['w1', 'w2'], positions=[4, 1])
c2 = LetterConstraint(variables=['w2', 'w3'], positions=[5, 1])
c3 = LetterConstraint(variables=['w3', 'w4'], positions=[5, 2])
c4 = LetterConstraint(variables=['w3', 'w6'], positions=[8, 0])
c5 = LetterConstraint(variables=['w4', 'w5'], positions=[0, 1])

problem = CSP(variables=map_variables, domains=domains, constraints=[c1, c2, c3, c4, c5])

initial_state = {}

search = BackTracking(problem=problem, value_criterion=random_assignment, var_criterion=degree_heuristic)

s = search.run(initial_state)

print(s)
