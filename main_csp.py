from csp.problem import *
from csp.backtracking import *
from input.australia import *

problem = CSP(variables=map_vars,
              domains=map_domains,
              constraints=map_cons)
search = BackTracking(problem=problem,
                      value_criterion=least_constraining_value)
initial_state = {}
print(search.run(initial_state))
