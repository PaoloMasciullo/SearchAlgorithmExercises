from csp.ac3 import AC3
from csp.contraints import DifferentValues, Constraint
from csp.problem import CSP
from exercises.graph_coloring.csp.backtracking import *

variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
domains = {var: ['r', 'g', 'b'] for var in variables}
constraints = [
    DifferentValues(['WA', 'NT']),
    DifferentValues(['NT', 'WA']),
    DifferentValues(['WA', 'SA']),
    DifferentValues(['SA', 'WA']),
    DifferentValues(['NT', 'Q']),
    DifferentValues(['Q', 'NT']),
    DifferentValues(['SA', 'Q']),
    DifferentValues(['Q', 'SA']),
    DifferentValues(['SA', 'NT']),
    DifferentValues(['NT', 'SA']),
    DifferentValues(['SA', 'NSW']),
    DifferentValues(['NSW', 'SA']),
    DifferentValues(['SA', 'V']),
    DifferentValues(['V', 'SA']),
    DifferentValues(['Q', 'NSW']),
    DifferentValues(['NSW', 'Q']),
    DifferentValues(['V', 'NSW']),
    DifferentValues(['NSW', 'V']),
]


problem = CSP(variables=variables, domains=domains, constraints=constraints)
initial_state = {}

print('Pre-process the problem running the Arc Consistency algorithm before the search')
print(f'\ndomains before the pre-processing step: \n{problem.domains}')
optimizer = AC3(csp=problem)
optimizer.run(state=initial_state)
print(f'\ndomains after the pre-processing step: \n{problem.domains}')


search = BackTracking(problem=problem, var_criterion=minimum_remaining_values, value_criterion=least_constraining_value)
print('\n\n---------------------------------------------------------------------------------------------------------------')
print('Apply search using Backtracking algorithm')
print(search.run(initial_state))
print('---------------------------------------------------------------------------------------------------------------')
print('\n\n---------------------------------------------------------------------------------------------------------------')
print('Apply search using Backtracking algorithm with forward checking')
print(search.run_with_forward_checking(initial_state, domains=problem.domains))
print('---------------------------------------------------------------------------------------------------------------')
print('\n\n---------------------------------------------------------------------------------------------------------------')
print('Apply search using Backtracking algorithm with arc consistency')
print(search.run_with_ac3(initial_state))
print('---------------------------------------------------------------------------------------------------------------')
