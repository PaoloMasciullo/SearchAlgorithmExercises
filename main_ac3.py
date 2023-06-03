from csp.problem import *
from csp.backtracking import *
from csp.ac3 import AC3
from input.australia import *

# Example 1
print('Example 1')
problem = CSP(variables=map_vars,
              domains=map_domains,
              constraints=map_cons)
state = problem.initial_state
optimizer = AC3(csp=problem)
optimizer.run(state)
print(problem.domains)

# Example 2
print('Example 2')
problem = CSP(variables=map_vars,
              domains=map_domains,
              constraints=map_cons)
act_state = {'WA': 'red', 'Q': 'green'}
problem.domains['WA'] = ['red']
problem.domains['Q'] = ['green']
optimizer = AC3(csp=problem)
optimizer.run(state)
print(problem.domains)
