from csp.ac3 import AC3
from csp.contraints import Constraint
from csp.problem import CSP
from exercises.csp_xyzk.backtracking import *


class Cxy(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] <= state[self.variables[1]]
        else:
            return True


class Cyx(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] >= state[self.variables[1]]
        else:
            return True


class Czy(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] < state[self.variables[1]]
        else:
            return True


class Cyz(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] > state[self.variables[1]]
        else:
            return True


class Ckz(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] == state[self.variables[1]]
        else:
            return True


variables = ['X', 'Y', 'Z', 'K']
domains = {
    'X': [i for i in range(5, 11)],
    'Y': [i for i in range(2, 16)],
    'Z': [i for i in range(4, 36)],
    'K': [i for i in range(7, 29)]
}
constraints = [Cxy(['X', 'Y']), Cyx(['Y', 'X']), Czy(['Z', 'Y']), Cyz(['Y', 'Z']), Ckz(['K', 'Z'])]

problem = CSP(variables=variables, domains=domains, constraints=constraints)
initial_state = {}

print('Pre-process the problem running the Arc Consistency algorithm before the search')
print(f'\ndomains before the pre-processing step: \n{problem.domains}')
optimizer = AC3(csp=problem)
optimizer.run(state=initial_state)
print(f'\ndomains after the pre-processing step: \n{problem.domains}')

search = BackTracking(problem=problem, var_criterion=degree_heuristic, value_criterion=least_constraining_value)

print('\n\nApply search using Backtracking algorithm')
print(search.run(state=initial_state))
print('\n\nApply search using Backtracking algorithm with forward checking')
print(search.run_with_forward_checking(state=initial_state, domains=problem.domains))
print('\n\nApply search using Backtracking algorithm with AC3')
print(search.run_with_ac3(state=initial_state))
